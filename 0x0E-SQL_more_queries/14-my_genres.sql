-- script uses database to list all genres of a given show
SELECT name
FROM tv_genres g
INNER JOIN tv_show_genres tv ON g.id=tv.genre_id
INNER JOIN tv_shows shows ON tv.show_id=shows.id 
AND shows.title='Dexter'
ORDER BY g.name ASC;
