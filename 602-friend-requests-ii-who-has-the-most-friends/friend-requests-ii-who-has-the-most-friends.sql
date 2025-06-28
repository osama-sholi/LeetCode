-- Write your PostgreSQL query statement below
SELECT COALESCE(rc.id, ac.id) id, (COALESCE(rc.count, 0) + COALESCE(ac.count, 0)) num
FROM 
(SELECT r.requester_id id, COUNT(*)
FROM RequestAccepted r
GROUP BY r.requester_id) rc
FULL JOIN
(SELECT r.accepter_id id, COUNT(*)
FROM RequestAccepted r
GROUP BY r.accepter_id) ac
ON rc.id = ac.id
ORDER BY num DESC
LIMIT 1
