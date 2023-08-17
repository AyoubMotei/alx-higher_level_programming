# Higher Level Programming - SQL Queries

This repository contains a collection of SQL scripts that perform various tasks related to managing a TV show database. The database contains information about TV shows, genres, and ratings. Each script is designed to address a specific task or query, and they are organized according to their respective tasks. Below is an overview of each task and its corresponding script.

## Task 0: My Privileges!
Script: [0-privileges.sql](./scripts/0-privileges.sql)

This script demonstrates how to create and manage privileges for MySQL users on the server. It includes commands to create users, grant privileges, and list privileges for the users `user_0d_1` and `user_0d_2` on the localhost.

## Task 1: Root User
Script: [1-create_user.sql](./scripts/1-create_user.sql)

This script creates a MySQL user named `user_0d_1` with all privileges on the server. If the user already exists, the script does not fail.

## Task 2: Read User
Script: [2-create_read_user.sql](./scripts/2-create_read_user.sql)

This script creates a MySQL user named `user_0d_2` with only the SELECT privilege on the database `hbtn_0d_2`. If the database or user already exists, the script does not fail.

## Task 3: Always a Name
Script: [3-force_name.sql](./scripts/3-force_name.sql)

This script creates a table named `force_name` in the MySQL server's database. The table has columns `id` (INT) and `name` (VARCHAR(256)) where `name` cannot be null. The script demonstrates handling constraints and default values.

## Task 4: ID Can't Be Null
Script: [4-never_empty.sql](./scripts/4-never_empty.sql)

This script creates a table named `id_not_null` with columns `id` (INT with default value 1) and `name` (VARCHAR(256)). The script shows how to enforce a default value constraint for a column.

## Task 5: Unique ID
Script: [5-unique_id.sql](./scripts/5-unique_id.sql)

This script creates a table named `unique_id` with columns `id` (INT with default value 1 and unique constraint) and `name` (VARCHAR(256)). It demonstrates how to enforce a unique constraint on a column.

## Task 6: States Table
Script: [6-states.sql](./scripts/6-states.sql)

This script creates a database named `hbtn_0d_usa` and a table named `states` within it. The table has columns `id` (INT, primary key, unique, auto-generated) and `name` (VARCHAR(256)).

## Task 7: Cities Table
Script: [7-cities.sql](./scripts/7-cities.sql)

This script creates a table named `cities` within the `hbtn_0d_usa` database. The table has columns `id` (INT, primary key, unique, auto-generated), `state_id` (INT, foreign key referencing `states.id`), and `name` (VARCHAR(256)).

## Task 8: Cities of California
Script: [8-cities_of_california_subquery.sql](./scripts/8-cities_of_california_subquery.sql)

This script lists all the cities of California from the `cities` table without using the JOIN keyword. It shows how to use subqueries to retrieve data.

## Task 9: Cities by States
Script: [9-cities_by_state_join.sql](./scripts/9-cities_by_state_join.sql)

This script lists all cities and their corresponding states using a JOIN operation between the `cities` and `states` tables.

## Task 10: Genre ID by Show
Script: [10-genre_id_by_show.sql](./scripts/10-genre_id_by_show.sql)

This script lists all shows and their associated genre IDs from the `tv_shows` and `tv_show_genres` tables.

## Task 11: Genre ID for All Shows
Script: [11-genre_id_all_shows.sql](./scripts/11-genre_id_all_shows.sql)

This script lists all shows and their associated genre IDs from the `tv_shows` and `tv_show_genres` tables. It displays NULL for shows without a genre.

## Task 12: No Genre
Script: [12-no_genre.sql](./scripts/12-no_genre.sql)

This script lists all shows without a genre from the `tv_shows` and `tv_show_genres` tables.

## Task 13: Number of Shows by Genre
Script: [13-count_shows_by_genre.sql](./scripts/13-count_shows_by_genre.sql)

This script lists the genres from the `tv_genres` table and displays the number of shows linked to each genre.

## Task 14: My Genres
Script: [14-my_genres.sql](./scripts/14-my_genres.sql)

This script lists all genres of the show "Dexter" from the `tv_genres` table.

## Task 15: Only Comedy
Script: [15-comedy_only.sql](./scripts/15-comedy_only.sql)

This script lists all Comedy shows from the `tv_shows` table.

## Task 16: List Shows and Genres
Script: [16-shows_by_genre.sql](./scripts/16-shows_by_genre.sql)

This script lists all shows and their linked genres from the `tv_shows` and `tv_genres` tables.

## Task 17: Not My Genre
Script: [100-not_my_genres.sql](./scripts/100-not_my_genres.sql)

This script lists all genres not linked to the show "Dexter" from the `tv_genres` table.

## Task 18: No Comedy Tonight!
Script: [101-not_a_comedy.sql](./scripts/101-not_a_comedy.sql)

This script lists all shows without the genre Comedy from the `tv_shows` and `tv_genres` tables.

## Task 19: Rotten Tomatoes
Script: [102-rating_shows.sql](./scripts/102-rating_shows.sql)

This script lists all shows by their rating from the `tv_shows` and `tv_show_ratings` tables.

## Task 20: Best Genre
Script: [103-rating_genres.sql](./scripts/103-rating_genres.sql)

This script lists all genres by their rating from the `tv_genres` and `tv_show_ratings` tables.

Each script demonstrates different SQL concepts and techniques, providing a comprehensive exploration of database querying and management. Feel free to explore and use these scripts as a reference.

