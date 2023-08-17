-- Create or modify the user user_0d_1
-- Description: This script creates the MySQL server user 'user_0d_1' with all privileges on the MySQL server.
-- The password for 'user_0d_1' is set to 'user_0d_1_pwd'. If the user already exists, the script does not fail.

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.*
TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
