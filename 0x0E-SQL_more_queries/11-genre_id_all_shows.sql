-- list all shows by name, genre
-- account for NULL, organize ascending
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
FULL OUTER JOIN show_id  
