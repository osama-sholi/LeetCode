-- Write your PostgreSQL query statement below
SELECT s.score, DENSE_RANK() OVER (ORDER BY score DESC) AS rank
FROM Scores AS s
ORDER BY rank