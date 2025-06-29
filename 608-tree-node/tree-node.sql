-- Write your PostgreSQL query statement below
SELECT DISTINCT t.id,
CASE
    WHEN t.p_id IS NULL THEN 'Root'
    WHEN t1.id IS NULL THEN 'Leaf'
    ELSE 'Inner'
END type
FROM Tree t LEFT JOIN Tree t1 ON t.id = t1.p_id
ORDER BY t.id