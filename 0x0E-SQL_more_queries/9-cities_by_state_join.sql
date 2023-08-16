-- List all cities with their corresponding states from the database hbtn_0d_usa
-- Description: This script retrieves and lists all the cities along with their corresponding state names from the 'cities' and 'states' tables.
-- The cities are joined with the states using the common 'state_id' column between the tables.
-- The results are sorted in ascending order by cities.id.

SELECT cities.id, cities.name, states.name FROM cities
JOIN states ON cities.state_id=states.id
ORDER BY cities.id;

