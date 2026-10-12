WITH ranked_salary AS
(
    SELECT
            department_id,
            D.name AS department,
            E.name AS employee,
            salary,
            DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) as rn
    FROM
            employee E
    JOIN
            department D
    ON
        E.department_id = D.id 
)
SELECT
    department,
    employee,
    salary
FROM
    ranked_salary
WHERE
    rn = 1