-- Script that creates a table called first_table in the current database in your MySQL server.
CREATE TABLE if NOT EXISTS second_table(id INT, name VARCHAR(256), score INT);
INSERT INTO second_table
VALUES(1, "John", 10),
    (2, "Alex", 3),
    (3, "Bob", 14),
    (4, "George", 8);