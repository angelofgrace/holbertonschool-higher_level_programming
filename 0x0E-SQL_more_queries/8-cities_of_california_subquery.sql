-- list all the elements of a table that reference another table's element
SELECT id, name FROM hbtn_0d_usa.cities
WHERE id IN (SELECT id FROM hbtn_0d_usa.states WHERE name = 'California')
ORDER BY id ASC;
