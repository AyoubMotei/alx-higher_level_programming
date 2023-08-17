-- Not my genre
-- Description: This script lists all genres not linked to the show Dexter in the hbtn_0d_tvshows database.
-- The tv_shows table contains only one record where title = Dexter (but the id can be different).
-- Each record displays the name of the genre.
-- Results are sorted in ascending order by the genre name.

SELECT name FROM tv_genres
WHERE tv_genres.id NOT IN (
      SELECT tv_genres.id FROM tv_genres
      JOIN tv_show_genres ON tv_genres.id=tv_show_genres.genre_id
      JOIN tv_shows ON tv_shows.id=tv_show_genres.show_id
      WHERE tv_shows.title = "DEXTER" )
ORDER BY tv_genres.name;

