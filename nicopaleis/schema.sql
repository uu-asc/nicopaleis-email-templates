DROP TABLE IF EXISTS layouts;
DROP TABLE IF EXISTS parameters;
DROP TABLE IF EXISTS snippets;
DROP TABLE IF EXISTS messages;

CREATE TABLE layouts (
    label       TEXT PRIMARY KEY,
    value       TEXT NOT NULL
);

CREATE TABLE parameters (
    label       TEXT PRIMARY KEY,
    value_nl    TEXT NOT NULL,
    value_en    TEXT
);

CREATE TABLE snippets (
    label       TEXT PRIMARY KEY,
    value_nl    TEXT NOT NULL,
    value_en    TEXT
);

CREATE TABLE messages (
    label       TEXT PRIMARY KEY,
    subject_nl  TEXT NOT NULL,
    subject_en  TEXT,
    body_nl     TEXT NOT NULL,
    body_en     TEXT,
    layout      INTEGER NOT NULL,
    FOREIGN KEY (layout) REFERENCES layout (label)
);
