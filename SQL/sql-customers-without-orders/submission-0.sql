-- Write your query below
SELECT
    DISTINCT cust.name
FROM 
    customers cust
    LEFT JOIN orders o
    ON cust.id = o.customer_id
WHERE 
    o.id IS NULL