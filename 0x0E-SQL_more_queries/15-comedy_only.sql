-- Only Comedy
-- Description: This script lists all Comedy shows in the hbtn_0d_tvshows database.
-- Each record displays the title of the show.
-- Results are sorted in ascending order by the show title.

SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN genres ON tv_show_genres.genre_id = genres.id
WHERE genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
