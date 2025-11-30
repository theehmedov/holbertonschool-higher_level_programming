-- Script.
SELECT
    t.title,
    g.name
FROM
    tv_shows AS t
LEFT JOIN
    tv_show_genres AS m
ON
    t.id = m.show_id
LEFT JOIN
    tv_genres AS g
ON
    g.id = m.genre_id
ORDER BY
    title ASC,
    name ASC;
