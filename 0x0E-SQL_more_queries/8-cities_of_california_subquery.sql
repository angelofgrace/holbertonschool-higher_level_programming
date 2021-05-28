-- list all the elements of a table that reference another table's element
SELECT id, name FROM cities
WHERE state_id IN (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
