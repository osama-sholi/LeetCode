# Write your MySQL query statement below
SELECT c1.visited_on, SUM(c2.amount) as amount, ROUND(SUM(c2.amount)/7, 2) as average_amount
FROM (
    SELECT DISTINCT visited_on FROM customer
    ) c1 JOIN customer c2 WHERE DATEDIFF(c1.visited_on, c2.visited_on) >= 0 and DATEDIFF(c1.visited_on, c2.visited_on) < 7
GROUP BY c1.visited_on
HAVING COUNT(DISTINCT c2.visited_on) = 7 