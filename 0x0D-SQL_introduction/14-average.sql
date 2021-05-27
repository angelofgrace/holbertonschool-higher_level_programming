-- compute the average score of all records
ALTER TABLE second_table
ADD average INT;
INSERT INTO second_table(average)
VALUES
(SELECT AVG(score) AS average FROM second_table);
