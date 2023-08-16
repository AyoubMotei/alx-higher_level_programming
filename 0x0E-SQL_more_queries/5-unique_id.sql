-- Create the table unique_id with specified columns and constraints
-- Description: This script creates the table 'unique_id' with columns 'id' (INT with default value 1 and unique constraint) and 'name' (VARCHAR(256)).
-- The 'id' column has a default value of 1 and must be unique. If the table already exists, the script does not fail.

CREATE TABLE IF NOT EXISTS unique_id
       (id INT DEFAULT 1,
       UNIQUE (ID),
       name VARCHAR(256));

