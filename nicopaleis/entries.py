from nicopaleis.db import get_db


def fetch_data(table, columns=None):
    if columns is None:
        columns = []
    if isinstance(columns, str):
        columns = [columns]
    columns = ['label'] + columns

    sql = (
        f"SELECT {','.join(col for col in columns)}"
        f"  FROM {table}"
        "  ORDER BY label;"
    )

    db = get_db()
    rows = db.execute(sql).fetchall()

    data = {}
    for row in rows:
        data[row['label']] = {col: row[col] for col in columns}
    return data


def put_data(table, data, columns):
    if isinstance(columns, str):
        columns = [columns]
    entries = [[k] + [v[col] for col in columns] for k, v in data.items()]
    db = get_db()
    db.execute(f"DELETE FROM {table};")
    db.executemany(
        "INSERT INTO"
        f"  {table} (label, {','.join(col for col in columns)})"
        f"  VALUES (?, {','.join(['?'] * len(columns))})", entries
    )
    db.commit()
    return None


def split(dct, name='value'):
    return {
        'nl': {k:v[f'{name}_nl'] for k,v in dct.items()},
        'en': {k:v[f'{name}_en'] for k,v in dct.items()},
    }
