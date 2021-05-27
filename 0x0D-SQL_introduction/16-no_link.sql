-- list all named records from a table, ordered
SELECT score, name 
FROM second_table 
WHERE name IS NOT NULL
ORDER BY score DESC;
