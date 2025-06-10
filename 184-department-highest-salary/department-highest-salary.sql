-- Write your PostgreSQL query statement below
WITH ed AS (
    SELECT 
    d.name AS "Department", 
    e.name AS "Employee", 
    e.salary AS "Salary",
    DENSE_RANK() OVER (PARTITION BY d.id ORDER BY e.salary DESC) AS rank
    FROM Employee AS e JOIN Department AS d ON e.departmentId = d.id
)

SELECT ed."Department", ed."Employee", ed."Salary"
FROM ed
WHERE ed.rank = 1