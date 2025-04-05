-- schema.sql
CREATE TABLE traffic (
    id SERIAL PRIMARY KEY,
    datetime TIMESTAMP,
    junction INT,
    vehicles INT
);
