-- Write your query below
SELECT
    DISTINCT l.page_id AS recommended_page
FROM
    likes l
JOIN (
    SELECT user2_id AS friend_id FROM friendship WHERE user1_id = 1
    UNION
    SELECT user1_id AS friend_id FROM friendship WHERE user2_id = 1
) f ON l.user_id = f.friend_id
WHERE
    l.page_id NOT IN (SELECT page_id FROM likes WHERE user_id = 1)