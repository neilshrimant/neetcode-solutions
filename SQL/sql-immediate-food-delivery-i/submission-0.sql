-- Write your query below
WITH scheduled_ord AS
(
SELECT
    SUM(CASE
            WHEN order_date = customer_pref_delivery_date
            THEN 1
            ELSE 0
        END) AS scheduled,
    COUNT(1) AS total
FROM 
    delivery
)
SELECT 
    ROUND(CAST(scheduled AS DECIMAL)/CAST(total AS DECIMAL) * 100, 2) AS immediate_percentage 
FROM 
    scheduled_ord