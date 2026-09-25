-- Write your query below
WITH combined AS (
    SELECT fail_date AS dt, 'failed' AS status FROM failed
    WHERE fail_date >= '2019-01-01' AND fail_date <= '2019-12-31'
    UNION
    SELECT success_date AS dt, 'succeeded' AS status FROM succeeded
    WHERE success_date >= '2019-01-01' AND success_date <= '2019-12-31'
),
grouped AS (
SELECT
    status,
    dt,
    CAST(dt AS date) - ROW_NUMBER() OVER (PARTITION BY status ORDER BY dt ASC) * INTERVAL '1 day' AS diff
FROM
    combined
)
SELECT
    status AS period_state,
    MIN(dt) AS start_date,
    MAX(dt) AS end_date
FROM
    grouped
GROUP BY
    status,
    diff
ORDER BY 
    2
