-- create a database representing the usa.
-- create a table of states, filled with names and ids.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL FOREIGN KEY (id) REFERENCES hbtn_0d_usa.states(id),
    name VARCHAR(256) NOT NULL);
