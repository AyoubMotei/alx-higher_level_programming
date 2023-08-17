-- List shows and their associated genre IDs
-- Description: This script lists all shows in the hbtn_0d_tvshows database along with their associated genre IDs.
-- If a show doesn't have a genre, it displays NULL. Results are sorted by title and genre ID.

SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;

