-- script lists all genres, counts number of shows linked to each
SELECT tv_genres.name AS genre, 
COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres g
LEFT JOIN tv_show_genres n ON g.id=n.genre_id
ORDER BY number_of_shows DESC;
