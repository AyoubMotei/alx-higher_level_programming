# ALX Higher Level Programming

This repository contains Python scripts that interact with a MySQL database using SQLAlchemy. Each script corresponds to a specific task and demonstrates various database operations.

## Tasks

### 0. Get all states
- Description: Write a script that lists all states from the database hbtn_0e_0_usa.
- Usage: `./0-select_states.py <mysql_username> <mysql_password> <database_name>`
- Results: Lists states in ascending order by ID.

### 1. Filter states
- Description: Write a script that lists all states with a name starting with 'N' from the database hbtn_0e_0_usa.
- Usage: `./1-filter_states.py <mysql_username> <mysql_password> <database_name>`
- Results: Lists states in ascending order by ID.

### 2. Filter states by user input
- Description: Write a script that displays all values in the states table where the name matches the argument.
- Usage: `./2-my_filter_states.py <mysql_username> <mysql_password> <database_name> <state_name>`
- Results: Lists states in ascending order by ID.

### 3. SQL Injection...
- Description: Write a script that displays all values in the states table where the name matches the argument, safe from SQL injection.
- Usage: `./3-my_safe_filter_states.py <mysql_username> <mysql_password> <database_name> <state_name>`
- Results: Lists states in ascending order by ID.

### 4. Cities by states
- Description: Write a script that lists all cities from the database hbtn_0e_4_usa.
- Usage: `./4-cities_by_state.py <mysql_username> <mysql_password> <database_name>`
- Results: Lists cities in ascending order by ID.

### 5. All cities by state
- Description: Write a script that lists all cities of a given state from the database hbtn_0e_4_usa.
- Usage: `./5-filter_cities.py <mysql_username> <mysql_password> <database_name> <state_name>`
- Results: Lists cities in ascending order by ID.

### 6. First state model
- Description: Create a State class using SQLAlchemy.
- Usage: `./6-model_state.py <mysql_username> <mysql_password> <database_name>`
- Results: Creates the 'states' table in the specified database.

### 7. All states via SQLAlchemy
- Description: Display all State objects from the database hbtn_0e_6_usa.
- Usage: `./7-model_state_fetch_all.py <mysql_username> <mysql_password> <database_name>`
- Results: Lists State objects with their IDs and names.

### 8. First state
- Description: Display the first State object from the database hbtn_0e_6_usa.
- Usage: `./8-model_state_fetch_first.py <mysql_username> <mysql_password> <database_name>`
- Results: Displays the first State object with its ID and name.

### 9. Contains 'a'
- Description: Display State objects that contain the letter 'a' from the database hbtn_0e_6_usa.
- Usage: `./9-model_state_filter_a.py <mysql_username> <mysql_password> <database_name>`
- Results: Lists State objects with their IDs and names.

### 10. Get a state
- Description: Print the ID of a State object with the specified name from the database hbtn_0e_6_usa.
- Usage: `./10-model_state_my_get.py <mysql_username> <mysql_password> <database_name> <state_name>`
- Results: Prints the State ID or "Not found."

### 11. Add a new state
- Description: Add a new State object "Louisiana" to the database hbtn_0e_6_usa.
- Usage: `./11-model_state_insert.py <mysql_username> <mysql_password> <database_name>`
- Results: Adds the State object and prints its ID.

### 12. Update a state
- Description: Change the name of a State object with ID 2 to "New Mexico" in the database hbtn_0e_6_usa.
- Usage: `./12-model_state_update_id_2.py <mysql_username> <mysql_password> <database_name>`
- Results: Updates the State name.

### 13. Delete states
- Description: Delete State objects with names containing the letter 'a' from the database hbtn_0e_6_usa.
- Usage: `./13-model_state_delete_a.py <mysql_username> <mysql_password> <database_name>`
- Results: Deletes State objects.

### 14. City relationship
- Description: Create a City class using SQLAlchemy and establish a relationship with the State class.
- Usage: `./relationship_city.py

