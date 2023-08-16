-- List all cities of California from the cities table without using the JOIN keyword
-- Description: This script retrieves and lists all the cities located in the state of California from the 'cities' table.
-- It achieves this by using a subquery to find the 'state_id' of California from the 'states' table and then filtering cities based on this 'state_id'.
-- The results are sorted in ascending order by cities.id.

SELECT id, name FROM cities
WHERE state_id = (
      SELECT id FROM states
      WHERE name = "California")
ORDER BY id;

