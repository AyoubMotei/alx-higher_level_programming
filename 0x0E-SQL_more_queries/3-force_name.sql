-- Create the table force_name with specified columns and constraints
-- Description: This script creates the table 'force_name' with columns 'id' (INT) and 'name' (VARCHAR(256)).
-- The 'name' column cannot be null. If the table already exists, the script does not fail.

CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);

