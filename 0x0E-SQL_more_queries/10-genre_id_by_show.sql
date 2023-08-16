-- List all shows with at least one linked genre from the hbtn_0d_tvshows database
-- Description: This script retrieves and lists all shows from the 'tv_shows' table that have at least one linked genre.
-- The genres are linked using the 'genre_id' column in the 'tv_show_genres' table.
-- Each record displays the show's title and the corresponding genre_id.
-- The results are sorted in ascending order by show title and genre_id.

SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;

