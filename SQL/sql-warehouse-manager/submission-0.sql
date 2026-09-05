SELECT
    w.name AS warehouse_name,
    SUM((p.width * p.length * p.height) * w.units) AS volume
FROM
    warehouse w
    LEFT JOIN products p ON w.product_id = p.product_id
GROUP BY
    w.name
ORDER BY
    w.name