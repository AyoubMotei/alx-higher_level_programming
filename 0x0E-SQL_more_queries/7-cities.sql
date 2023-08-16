-- Create the database hbtn_0d_usa and the table cities within it
-- Description: This script creates the database 'hbtn_0d_usa' if it doesn't exist, and then creates the table 'cities' within the database.
-- The 'cities' table has columns 'id' (INT, primary key, unique, auto-generated), 'state_id' (INT, foreign key referencing states.id), and 'name' (VARCHAR(256)).
-- The 'state_id' column references the 'id' column of the 'states' table.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
       id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
       state_id INT NOT NULL,
       FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id),
       name VARCHAR(256) NOT NULL);

