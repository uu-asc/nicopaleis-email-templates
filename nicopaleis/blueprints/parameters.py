from flask import (
    Blueprint, redirect, render_template, request, url_for
)

from nicopaleis.entries import fetch_data, put_data


bp = Blueprint('parameters', __name__, url_prefix='/nicopaleis/parameters')


@bp.route('/', methods=('GET', 'POST'))
def manage():
    table = 'parameters'
    fields = ['value_nl', 'value_en']
    data = fetch_data(table, fields)
    if request.method == 'POST':
        new_data = request.get_json()
        put_data(table, new_data, fields)
        return redirect(url_for('parameters.manage'))
    return render_template(
        'manager/parameters.html',
        module='parameters',
        data=data,
        fields=fields,
    )
