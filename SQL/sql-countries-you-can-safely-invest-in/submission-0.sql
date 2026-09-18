-- Write your query below
SELECT
    c.name AS country
FROM
    person p
    JOIN country c ON SUBSTRING(p.phone_number,1,3) = c.country_code
    JOIN calls cl ON p.id = cl.caller_id OR p.id = cl.callee_id
GROUP BY
    c.name
HAVING
    AVG(cl.duration) > (SELECT AVG(duration) FROM calls)