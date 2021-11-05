DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS classes;

CREATE TABLE classes(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    date VARCHAR(255),
    time FLOAT,
    duration INT
);

CREATE TABLE members(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    second_name VARCHAR(255),
    phone_no VARCHAR(255),
    class_id INT REFERENCES classes(id) ON DELETE CASCADE
);