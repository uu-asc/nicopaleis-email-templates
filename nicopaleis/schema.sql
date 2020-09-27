DROP TABLE IF EXISTS layouts;
DROP TABLE IF EXISTS parameters;
DROP TABLE IF EXISTS snippets;
DROP TABLE IF EXISTS settings;
DROP TABLE IF EXISTS messages;

CREATE TABLE layouts (
    label                       TEXT PRIMARY KEY,
    value                       TEXT NOT NULL
);

CREATE TABLE parameters (
    label                       TEXT PRIMARY KEY,
    value_nl                    TEXT NOT NULL,
    value_en                    TEXT
);

CREATE TABLE snippets (
    label                       TEXT PRIMARY KEY,
    value_nl                    TEXT NOT NULL,
    value_en                    TEXT
);

CREATE TABLE settings (
    label                       TEXT PRIMARY KEY,
    faculteit                   TEXT,
    communicatiekanaal          TEXT,
    type_mededeling             TEXT,
    muteerbaar                  TEXT,
    actueel                     TEXT,
    formaat                     TEXT,
    e_mail_adres_1              TEXT,
    antwoordadres               TEXT,
    ander_antwoordadres         TEXT,
    verstuur_in_context         TEXT,
    verstuur_vanaf_tijdstip     TEXT,
    zichtbaar_in_student        TEXT,
    documentset                 TEXT,
    keuze_zichtbaar_in_document TEXT,
    toon_antwoordadres_no_reply TEXT,
    toon_antwoordadres_mijzelf  TEXT,
    toon_antwoordadres_opgeven  TEXT
);

CREATE TABLE messages (
    label                       TEXT PRIMARY KEY,
    subject_nl                  TEXT NOT NULL,
    subject_en                  TEXT,
    body_nl                     TEXT NOT NULL,
    body_en                     TEXT,
    layout                      TEXT,
    settings                    TEXT,
    FOREIGN KEY (layout)   REFERENCES layout   (label),
    FOREIGN KEY (settings) REFERENCES settings (label)
);
