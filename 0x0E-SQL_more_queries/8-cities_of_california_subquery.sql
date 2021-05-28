-- list all the elements of a table that reference another table's element
SELECT id from cities
WHERE states.name = 'California';
