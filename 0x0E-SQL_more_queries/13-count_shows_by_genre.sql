-- Count shows by genre
-- Description: This script lists all genres in the hbtn_0d_tvshows database and displays the number of shows linked to each genre.
-- Each record displays the genre and the number of shows linked to that genre.
-- Results are sorted in descending order by the number of shows linked.

SELECT name AS genre, COUNT(*) AS number_of_shows FROM tv_genres
JOIN tv_show_genres ON id=tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;

