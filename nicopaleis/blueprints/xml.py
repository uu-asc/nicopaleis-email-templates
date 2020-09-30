from string import Template

from markdown import markdown
from flask import (
    Blueprint,
    render_template,
    request,
    make_response,
    jsonify,
)

from nicopaleis.db import get_db
from nicopaleis.entries import fetch_data, put_data, split


bp = Blueprint('xml', __name__, url_prefix='/nicopaleis/xml')


def prime(string, parameters):
    "Return string where all `parameters` have been substituted in `string`."

    template = Template(string)
    return template.safe_substitute(parameters)


def fix(string):
    "Convert special characters to entity references within xml tags."

    replacements = {
        '<br>': '<br />',
        '<hr>': '<hr />',
        '&':    '&amp;',
        '<':    '&lt;',
        '>':    '&gt;',
        '"':    '&quot;',
        "'":    '&apos;',
    }
    for replacement in replacements.items():
        string = string.replace(*replacement)
    return string


def taggify(tag, value):
    "Return <`tag`>`value`</`tag`>."

    if value == '':
        return ''
    tag = tag.upper()
    return f"<{tag}>{value}</{tag}>"


def prep_snippets(snip, param):
    """Split snippets `snip` into separate languages
    and substitute parameters `param` with their values."""

    snip = split(snip)
    snip['nl'] = {k:prime(v, param['nl']) for k,v in snip['nl'].items()}
    snip['en'] = {k:prime(v, param['en']) for k,v in snip['en'].items()}
    return snip


def build_xml(selection, messages):
    "Return all selected messages as xml."

    content = []
    for message in messages:
        if not message['mededeling'] in selection:
            continue
        row = '\n'.join([taggify(k, v) for k,v in message.items() if v != ''])
        content.append(f"<OSU_MEDEDELING_ROW>\n{row}</OSU_MEDEDELING_ROW>\n")
    content = [item for item in content if item != '']
    content = '\n'.join(content)
    return (
        '<?xml version="1.0"?>\n'
        '<ROWSET>\n'
        '<ROW>\n'
        '     <OSU_MEDEDELING>\n'
        f'{content}\n'
        '     </OSU_MEDEDELING>\n'
        '</ROW>\n'
        '</ROWSET>\n'
    )


@bp.route('/', methods=('GET', 'POST'))
def manage():
    parameters = split(fetch_data('parameters', ['value_nl', 'value_en']))
    snippets = fetch_data('snippets', ['value_nl', 'value_en'])
    snippets = prep_snippets(snippets, parameters)
    variables = {k:{**parameters[k], **snippets[k]} for k in parameters}

    sql = """
        SELECT
            m.label            as mededeling,
            subject_nl         as koptekst,
            subject_en         as koptekst_en,
            body_nl            as inhoud,
            body_en            as inhoud_en,
            value              as layout,
            faculteit,
            communicatiekanaal,
            type_mededeling,
            muteerbaar,
            actueel,
            formaat,
            e_mail_adres_1,
            antwoordadres,
            ander_antwoordadres,
            verstuur_in_context,
            verstuur_vanaf_tijdstip,
            zichtbaar_in_student,
            documentset,
            keuze_zichtbaar_in_document,
            toon_antwoordadres_no_reply,
            toon_antwoordadres_mijzelf,
            toon_antwoordadres_opgeven
        FROM
            messages m
        INNER JOIN
            settings s
            ON m.settings = s.label
        INNER JOIN
            layouts l
            ON m.layout = l.label;
    """

    db = get_db()
    messages = [dict(row) for row in db.execute(sql).fetchall()]

    for msg in messages:
        layout_nl = prime(msg['layout'], variables['nl'])
        layout_en = prime(msg['layout'], variables['en'])

        msg['koptekst'] = prime(msg['koptekst'], variables['nl'])
        msg['koptekst_en'] = prime(msg['koptekst_en'], variables['en'])
        msg['koptekst_nls'] = msg['koptekst']

        msg['inhoud'] = markdown(prime(msg['inhoud'], variables['nl']))
        msg['inhoud_en'] = markdown(prime(msg['inhoud_en'], variables['en']))

        msg['inhoud'] = fix(prime(layout_nl, dict(content=msg['inhoud'])))
        msg['inhoud_en'] = fix(prime(layout_en, dict(content=msg['inhoud_en'])))
        msg['inhoud_nls'] = msg['inhoud']

        msg['omschrijving'] = msg['koptekst']
        msg['omschrijving_en'] = msg['koptekst_en']
        msg['omschrijving_nls'] = msg['koptekst']

        del msg['layout']

    if request.method == 'POST':
        selection = request.get_json()
        xml = build_xml(selection, messages)
        return make_response(jsonify(xml))
    return render_template(
        'manager/xml.html',
        module='xml',
        data = [msg['mededeling'] for msg in messages]
    )
