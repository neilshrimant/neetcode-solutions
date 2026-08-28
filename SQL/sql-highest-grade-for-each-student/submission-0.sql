-- Write your query below
WITH grouped_score AS (
    SELECT
        student_id,
        exam_id,
        score,
        ROW_NUMBER() OVER (
            PARTITION BY student_id
            ORDER BY score DESC, exam_id ASC
        ) AS rn
    FROM 
        exam_results
)
SELECT 
    student_id,
    exam_id,
    score
FROM 
    grouped_score
WHERE
    rn = 1
