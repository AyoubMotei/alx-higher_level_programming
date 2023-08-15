# ALX Higher Level Programming - SQL Introduction

Welcome to the ALX Higher Level Programming SQL Introduction repository! In this repository, you will find a collection of SQL scripts that cover various tasks related to working with MySQL databases. Each script is designed to help you practice and improve your SQL skills. Below, you'll find a brief description of each task along with the corresponding script files.

## Task 0: List Databases

Script: [0-list_databases.sql](./0x0D-SQL_introduction/0-list_databases.sql)

This script lists all the databases present on your MySQL server.

## Task 1: Create a Database

Script: [1-create_database_if_missing.sql](./0x0D-SQL_introduction/1-create_database_if_missing.sql)

This script creates a database named `hbtn_0c_0` on your MySQL server if it does not already exist.

## Task 2: Delete a Database

Script: [2-remove_database.sql](./0x0D-SQL_introduction/2-remove_database.sql)

This script deletes the `hbtn_0c_0` database from your MySQL server if it exists.

## Task 3: List Tables

Script: [3-list_tables.sql](./0x0D-SQL_introduction/3-list_tables.sql)

This script lists all the tables in a specified database on your MySQL server.

## Task 4: First Table

Script: [4-first_table.sql](./0x0D-SQL_introduction/4-first_table.sql)

This script creates a table named `first_table` with columns `id` (INT) and `name` (VARCHAR(256)) in the `hbtn_0c_0` database.

## Task 5: Full Description

Script: [5-full_table.sql](./0x0D-SQL_introduction/5-full_table.sql)

This script displays the full description of the `first_table` in the `hbtn_0c_0` database.

## Task 6: List All in Table

Script: [6-list_values.sql](./0x0D-SQL_introduction/6-list_values.sql)

This script lists all the rows in the `first_table` of the `hbtn_0c_0` database.

## Task 7: First Add

Script: [7-insert_value.sql](./0x0D-SQL_introduction/7-insert_value.sql)

This script inserts a new row into the `first_table` of the `hbtn_0c_0` database.

## Task 8: Count 89

Script: [8-count_89.sql](./0x0D-SQL_introduction/8-count_89.sql)

This script counts the number of records with `id = 89` in the `first_table` of the `hbtn_0c_0` database.

## Task 9: Full Creation

Script: [9-full_creation.sql](./0x0D-SQL_introduction/9-full_creation.sql)

This script creates a table named `second_table` with columns `id` (INT), `name` (VARCHAR(256)), and `score` (INT) in the `hbtn_0c_0` database and adds multiple rows.

## Task 10: List by Best

Script: [10-top_score.sql](./0x0D-SQL_introduction/10-top_score.sql)

This script lists all records in the `second_table` of the `hbtn_0c_0` database, ordered by score (top first).

## Task 11: Select the Best

Script: [11-best_score.sql](./0x0D-SQL_introduction/11-best_score.sql)

This script lists records with a score >= 10 in the `second_table` of the `hbtn_0c_0` database, ordered by score (top first).

## Task 12: Cheating is Bad

Script: [12-no_cheating.sql](./0x0D-SQL_introduction/12-no_cheating.sql)

This script updates the score of a record with the name "Bob" to 10 in the `second_table` of the `hbtn_0c_0` database.

## Task 13: Score Too Low

Script: [13-change_class.sql](./0x0D-SQL_introduction/13-change_class.sql)

This script removes records with a score <= 5 from the `second_table` of the `hbtn_0c_0` database.

## Task 14: Average

Script: [14-average.sql](./0x0D-SQL_introduction/14-average.sql)

This script computes the average score of all records in the `second_table` of the `hbtn_0c_0` database.

## Task 15: Number by Score

Script: [15-groups.sql](./0x0D-SQL_introduction/15-groups.sql)

This script lists the number of records with the same score in the `second_table` of the `hbtn_0c_0` database, sorted by the number of records (descending).

## Task 16: Say My Name

Script: [16-no_link.sql](./0x0D-SQL_introduction/16-no_link.sql)

This script lists records in the `second_table` of the `hbtn_0c_0` database, displaying the score and the name (in this order), excluding rows without a name value, and ordered by descending score.

## Task 17: Go to UTF8

Script: [100-move_to_utf8.sql](./0x0D-SQL_introduction/100-move_to_utf8.sql)

This script converts the `hbtn_0c_0` database, the `first_table` table, and the `name` field in the `first_table` to UTF8 (utf8mb4, collate utf8mb4_unicode_ci).

## Task 18: Temperatures #0

Script: [101-avg_temperatures.sql](./0x0D-SQL_introduction/101-avg_temperatures.sql)

This script computes and displays the average temperature (Fahrenheit) by city in the `hbtn_0c_0` database, ordered by temperature (descending).

## Task 19: Temperatures #1

Script: [102-top_city.sql](./0x0D-SQL_introduction/102-top_city.sql)

This script lists the top 3 cities with the highest average temperatures during July and August in the `hbtn_0c_0` database, ordered by temperature (descending).

## Task 20: Temperatures #2

Script: [103-max_state.sql](./0x0D-SQL_introduction/103-max_state.sql)

This script displays the maximum temperature of each state in the `hbtn_0c_0` database, ordered by state name.

Feel free to explore, modify, and use these scripts to enhance your SQL skills and understanding of database management using MySQL. Happy coding!

