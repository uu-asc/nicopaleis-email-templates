from flask import (
    Blueprint, redirect, render_template, request, url_for
)

from nicopaleis.entries import fetch_data, put_data


bp = Blueprint('layouts', __name__, url_prefix='/nicopaleis/layouts')


@bp.route('/', methods=('GET', 'POST'))
def manage():
    table = 'layouts'
    values = ['value']
    data = fetch_data(table, values)
    if request.method == 'POST':
        new_data = request.get_json()
        put_data(table, new_data, values)
        return redirect(url_for('layouts.manage'))
    return render_template(
        'manager/layouts.html',
        module='layouts',
        data=data,
        values=values,
    )
