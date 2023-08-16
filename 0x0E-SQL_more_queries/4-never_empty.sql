-- Create the table id_not_null with specified columns and constraints
-- Description: This script creates the table 'id_not_null' with columns 'id' (INT with default value 1) and 'name' (VARCHAR(256)).
-- The 'id' column has a default value of 1. If the table already exists, the script does not fail.

CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));

