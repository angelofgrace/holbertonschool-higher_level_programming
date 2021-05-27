-- create a database and a user with select privilege.
IF DB_ID('hbtn_0d_2') IS NOT NULL
CREATE DATABASE hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT PRIVILEGES ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
