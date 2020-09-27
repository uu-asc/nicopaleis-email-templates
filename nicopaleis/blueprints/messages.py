from string import Template

from flask import (
    Blueprint, redirect, render_template, request, url_for
)

from nicopaleis.entries import fetch_data, put_data, split


bp = Blueprint('messages', __name__, url_prefix='/nicopaleis/messages')


def prime(string, parameters):
    template = Template(string)
    return template.safe_substitute(parameters)


@bp.route('/', methods=('GET', 'POST'))
def manage():
    layouts = fetch_data('layouts', ['value'])
    parameters = split(fetch_data('parameters', ['value_nl', 'value_en']))
    snippets = split(fetch_data('snippets', ['value_nl', 'value_en']))

    snippets = {
        'nl': {k:prime(v, parameters['nl']) for k,v in snippets['nl'].items()},
        'en': {k:prime(v, parameters['en']) for k,v in snippets['en'].items()},
    }

    table = 'messages'
    values = [
        'subject_nl',
        'subject_en',
        'body_nl',
        'body_en',
        'layout',
    ]
    data = fetch_data(table, fields)
    if request.method == 'POST':
        new_data = request.get_json()
        put_data(table, new_data, fields)
        return redirect(url_for('messages.manage'))
    return render_template(
        'manager/messages.html',
        module='messages',
        layouts=layouts,
        parameters=parameters,
        snippets=snippets,
        data=data,
        fields=fields,
    )
