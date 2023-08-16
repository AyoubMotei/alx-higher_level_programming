-- Create the database hbtn_0d_usa and the table states within it
-- Description: This script creates the database 'hbtn_0d_usa' if it doesn't exist, and then creates the table 'states' within the database.
-- The 'states' table has columns 'id' (INT, primary key, unique, auto-generated) and 'name' (VARCHAR(256)), where 'id' cannot be null and is unique.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
       id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(256) NOT NULL);

