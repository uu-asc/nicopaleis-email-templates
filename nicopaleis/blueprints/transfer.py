from flask import (
    Blueprint, redirect, render_template, request, url_for
)

from nicopaleis.entries import fetch_data, put_data


bp = Blueprint('transfer', __name__, url_prefix='/transfer')


@bp.route('/', methods=('GET', 'POST'))
def manage():
    def convert(path):
        return (
            path.read_text(encoding='utf-8')
            .replace('[', '$')
            .replace(']', '')
        )


    # TRANSFER PARAMETERS
    with open('transfer/uu_csa_content.csv', 'r') as f:
        csv = f.read().strip('\n')

    lines = csv.split('\n')
    rows = [[cell for cell in line.split(';')] for line in lines[1:]]
    data = {}
    columns = ['value_nl', 'value_en']
    for row in rows:
        data[row[0]] = {columns[0]: row[1], columns[1]: row[2]}
    put_data('parameters', data, columns)


    # TRANSFER SNIPPETS
    from pathlib import Path
    path_nl = Path('transfer/snip_nl')
    path_en = Path('transfer/snip_en')

    columns = ['value_nl', 'value_en']
    data = {}
    for path in path_nl.glob('*'):
        data[path.stem] = {
            'value_nl': convert(path_nl / path.name),
            'value_en': convert(path_en / path.name),
        }
    put_data('snippets', data, columns)


    # TRANSFER CONTENT
    from pathlib import Path
    path = Path('transfer/content/betaling')

    columns = ['subject_nl', 'subject_en', 'body_nl', 'body_en', 'layout']
    data = {}
    for p in path.glob('*-nl.md'):
        data[p.stem.lower().replace('-', '_')[:-3]] = {
            'subject_nl': '',
            'subject_en': '',
            'body_nl': convert(path / f"{p.stem}.md"),
            'body_en': convert(path / f"{p.stem[:-3]}-en.md"),
            'layout': 'csa_template',
        }
    put_data('messages', data, columns)

    return "transfer complete"
