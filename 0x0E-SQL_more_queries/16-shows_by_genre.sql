-- script lists all shows and all genres linked to each
SELECT title, name
FROM tv_shows show
LEFT JOIN tv_show_genres n ON show.id=n.show_id 
LEFT JOIN tv_genres genre ON n.genre_id=genre.id 
ORDER BY title, name ASC;
