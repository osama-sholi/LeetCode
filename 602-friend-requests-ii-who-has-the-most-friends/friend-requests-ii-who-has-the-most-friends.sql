-- Write your PostgreSQL query statement below
SELECT ra.id, COUNT(*) num
FROM 
(SELECT r.requester_id id
FROM RequestAccepted r
UNION ALL
SELECT r.accepter_id id
FROM RequestAccepted r) ra
GROUP BY ra.id
ORDER BY num DESC
LIMIT 1
