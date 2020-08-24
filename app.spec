# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

added_files =[
    ('nicopaleis/templates/*.*', 'nicopaleis/templates'),
    ('nicopaleis/templates/manager/*.*', 'nicopaleis/templates/manager'),
    ('nicopaleis/static/*.*', 'nicopaleis/static'),
    ('nicopaleis/static/scripts/*.*', 'nicopaleis/static/scripts'),
    ('instance/*.*', 'var/nicopaleis-instance'),
    ]

a = Analysis(
    ['app.py'],
    pathex=['C:\\Users\\lcvri\\projects_lc\\dev\\nicopaleis'],
    binaries=[],
    datas=added_files,
    hiddenimports=['jinja2.ext', 'sqlite3'],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=block_cipher,
)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='nicopaleis',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    icon='nicopaleis\\static\\tajmahal.ico',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='app',
)
