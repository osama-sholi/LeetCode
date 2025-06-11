-- Write your PostgreSQL query statement below
SELECT ROUND(SUM(i.tiv_2016)::numeric, 2) AS tiv_2016
FROM Insurance i
WHERE EXISTS (
    SELECT 1
    FROM Insurance i1
    WHERE i1.pid != i.pid AND i1.tiv_2015 = i.tiv_2015
) AND NOT EXISTS (
    SELECT 1
    FROM Insurance i1
    WHERE i1.pid != i.pid AND i1.lat = i.lat AND i1.lon = i.lon
)
