-- script lists all shows of one genre in database
SELECT title
FROM tv_shows shows
INNER JOIN tv_show_genres n ON shows.id=n.show_id
INNER JOIN tv_genres genre ON n.genre_id=genre.id
AND genre.name = 'Comedy'
ORDER BY shows.title ASC;
