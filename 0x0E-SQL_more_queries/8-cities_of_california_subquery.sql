-- list all the elements of a table that reference another table's element
SELECT id FROM cities
WHERE states.name = 'California';
