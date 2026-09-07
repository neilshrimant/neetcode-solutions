-- Write your query below
WITH most_orders AS (
    SELECT 
        COUNT(*) AS num_orders,
        customer_number
    FROM
        orders
    GROUP BY
        customer_number
),
ranked AS (
SELECT
    row_number() OVER (ORDER BY num_orders DESC) as rn,
    customer_number
FROM
    most_orders
)
SELECT
    customer_number
FROM
    ranked
WHERE
    rn = 1
