-- Only Comedy
-- Description: This script lists all Comedy shows in the hbtn_0d_tvshows database.
-- Each record displays the title of the show.
-- Results are sorted in ascending order by the show title.

SELECT tv_shows.title
FROM tv_shows
INNER JOIN tv_show_genres m ON tv_shows.id = m.show_id
INNER JOIN tv_genres g ON m.genre_id = g.id
WHERE g.name = 'Comedy'
ORDER BY tv_shows.title ASC;