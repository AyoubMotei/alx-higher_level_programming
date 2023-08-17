-- List shows without a genre
-- Description: This script lists all shows in the hbtn_0d_tvshows database that do not have a genre linked.
-- Each record displays the show's title and genre ID (NULL for shows without a genre).
-- Results are sorted by title and genre ID.

SELECT title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON id=tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NULL
ORDER BY title, tv_show_genres.genre_id;

