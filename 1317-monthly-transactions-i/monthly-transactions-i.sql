-- Write your PostgreSQL query statement below
-- SELECT t.month, t.country, t.trans_count, COALESCE(t1.approved_count, 0) approved_count, t.trans_total_amount, COALESCE(t1.approved_total_amount, 0) approved_total_amount
-- FROM 
-- (
--     SELECT country, TO_CHAR(trans_date, 'YYYY-MM') AS month, SUM(amount) trans_total_amount, COUNT(*) trans_count
--     FROM Transactions
--     GROUP BY country, TO_CHAR(trans_date, 'YYYY-MM')
-- ) t FULL JOIN
-- (
--     SELECT country, TO_CHAR(trans_date, 'YYYY-MM') AS month, SUM(amount) approved_total_amount, COUNT(*) approved_count
--     FROM Transactions
--     WHERE state = 'approved'
--     GROUP BY country, TO_CHAR(trans_date, 'YYYY-MM')
-- ) t1 ON COALESCE(t.country, 'null') = COALESCE(t1.country, 'null') AND t.month = t1.month
SELECT TO_CHAR(trans_date, 'YYYY-MM') AS month, country, COUNT(*) trans_count, COUNT(CASE WHEN state = 'approved' THEN 1 END) approved_count, SUM(amount) trans_total_amount, COALESCE(SUM(CASE WHEN state = 'approved' THEN amount END),0) approved_total_amount
FROM Transactions
GROUP BY country, TO_CHAR(trans_date, 'YYYY-MM')
