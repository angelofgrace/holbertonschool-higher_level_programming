-- create a database representing the usa.
-- create a table of states, filled with names and ids.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS 'states' (
    id INT IDENTITY PRIMARY KEY,
    name VARCHAR(256) NOT NULL);
