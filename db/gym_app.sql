DROP TABLE IF EXISTS schedule;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS classes;


CREATE TABLE classes(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    date VARCHAR(255),
    time VARCHAR(255),
    duration INT,
    fully_booked BOOLEAN
);

CREATE TABLE members(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    second_name VARCHAR(255),
    phone_no VARCHAR(255)
);

CREATE TABLE schedule(
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) on DELETE CASCADE,
    class_id INT REFERENCES classes(id) on DELETE CASCADE
);