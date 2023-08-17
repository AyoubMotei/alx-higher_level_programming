-- List shows and genres
-- Description: This script lists all shows and their linked genres from the hbtn_0d_tvshows database.
-- If a show doesn't have a genre, NULL is displayed in the genre column.
-- Each record displays the title of the show and the name of the genre.
-- Results are sorted in ascending order by the show title and genre name.

SELECT title, tv_genres.name FROM tv_shows
LEFT JOIN tv_show_genres ON id=tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY title, tv_genres.name;

