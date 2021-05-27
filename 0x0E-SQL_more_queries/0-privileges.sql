-- list all priveleges of two MySQL users
-- expected failure if executing without privilege
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
