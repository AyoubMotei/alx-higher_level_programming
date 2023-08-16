-- Create or modify the user user_0d_2 and database hbtn_0d_2
-- Description: This script creates the MySQL user 'user_0d_2' with SELECT privilege on the database 'hbtn_0d_2'.
-- The password for 'user_0d_2' is set to 'user_0d_2_pwd'. If the user or database already exists, the script does not fail.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;

