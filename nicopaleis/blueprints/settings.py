import json

from flask import (
    Blueprint, redirect, render_template, request, url_for, current_app
)

from nicopaleis.entries import fetch_data, put_data


bp = Blueprint('settings', __name__, url_prefix='/nicopaleis/settings')


@bp.route('/', methods=('GET', 'POST'))
def manage():
    with current_app.open_resource('reference_table.json') as f:
        dropdown = json.load(f)

    table = 'settings'
    fields = [
        'faculteit',
        'communicatiekanaal',
        'type_mededeling',
        'muteerbaar',
        'actueel',
        'formaat',
        'e_mail_adres_1',
        'antwoordadres',
        'ander_antwoordadres',
        'verstuur_in_context',
        'zichtbaar_in_student',
        'documentset',
        'verstuur_vanaf_tijdstip',
        'keuze_zichtbaar_in_document',
        'toon_antwoordadres_no_reply',
        'toon_antwoordadres_mijzelf',
        'toon_antwoordadres_opgeven',
    ]
    data = fetch_data(table, fields)
    if request.method == 'POST':
        new_data = request.get_json()

        checkboxes = [
            'muteerbaar',
            'actueel',
            'zichtbaar_in_student',
            'keuze_zichtbaar_in_document',
            'toon_antwoordadres_no_reply',
            'toon_antwoordadres_mijzelf',
            'toon_antwoordadres_opgeven',
        ]

        for item in new_data.values():
            for checkbox in checkboxes:
                if item[checkbox] == '':
                    item[checkbox] = 'N'

        put_data(table, new_data, fields)
        return redirect(url_for('settings.manage'))
    return render_template(
        'manager/settings.html',
        module='settings',
        data=data,
        fields=fields,
        dropdown=dropdown,
    )
