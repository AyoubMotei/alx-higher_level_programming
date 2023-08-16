-- This script lists records of the second_table with names, ordered by descending score.
SELECT score, name
FROM second_table
HAVING name IS NOT NULL
ORDER BY score DESC;

