-- Best genre
-- Description: This script lists all genres in the hbtn_0d_tvshows_rate database by their rating sum.
-- Each record displays the name of the genre and the rating sum.
-- Results are sorted in descending order by the rating.

SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS rating -- Query to join tables
FROM tv_genres
JOIN tv_show_genres
     ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows
     ON tv_show_genres.show_id = tv_shows.id
JOIN tv_show_ratings
     ON tv_show_ratings.show_id = tv_shows.id
GROUP BY tv_genres.name
ORDER BY rating DESC;
