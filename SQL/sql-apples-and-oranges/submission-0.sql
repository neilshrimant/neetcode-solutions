-- Write your query below
WITH apples_sold AS
(
    SELECT
        SUM(sold_num) AS total_apples,
        sale_date
    FROM
        sales
    WHERE
        fruit = 'apples'
    GROUP BY sale_date
),
oranges_sold AS
(
    SELECT
        SUM(sold_num) AS total_oranges,
        sale_date
    FROM
        sales
    WHERE
        fruit = 'oranges'
    GROUP BY sale_date
)
SELECT
    A.sale_date,
    total_apples - total_oranges AS diff
FROM
    apples_sold AS A
    JOIN oranges_sold AS O ON A.sale_date = O.sale_date
