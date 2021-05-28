-- script lists all shows contained without a linked genre
SELECT title, genre_id
FROM tv_shows a
LEFT JOIN tv_show_genres b ON a.id=b.show_id WHERE b.show_id IS NULL
ORDER BY a.title, b.genre_id ASC;

