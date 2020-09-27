from flask import (
    Blueprint, redirect, render_template, request, url_for
)

from nicopaleis.entries import fetch_data, put_data, split


bp = Blueprint('snippets', __name__, url_prefix='/nicopaleis/snippets')


@bp.route('/', methods=('GET', 'POST'))
def manage():
    table = 'snippets'
    fields = ['value_nl', 'value_en']
    parameters = split(fetch_data('parameters', fields))
    data = fetch_data(table, fields)
    if request.method == 'POST':
        new_data = request.get_json()
        put_data(table, new_data, fields)
        return redirect(url_for('snippets.manage'))
    return render_template(
        'manager/snippets.html',
        module='snippets',
        parameters=parameters,
        data=data,
        fields=fields,
    )
