from flask import (
    Blueprint, redirect, render_template, request, url_for
)

from nicopaleis.entries import fetch_data, put_data


bp = Blueprint('snippets', __name__, url_prefix='/nicopaleis/snippets')


@bp.route('/', methods=('GET', 'POST'))
def manage():
    table = 'snippets'
    values = ['value_nl', 'value_en']
    data = fetch_data(table, values)
    if request.method == 'POST':
        new_data = request.get_json()
        put_data(table, new_data, values)
        return redirect(url_for('snippets.manage'))
    return render_template(
        'manager/snippets.html',
        module='snippets',
        data=data,
        values=values,
    )
