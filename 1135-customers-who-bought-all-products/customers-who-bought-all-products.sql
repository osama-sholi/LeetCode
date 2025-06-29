-- Write your PostgreSQL query statement below
SELECT c.customer_id
FROM (
    SELECT DISTINCT customer_id, product_key
    FROM Customer
) c
GROUP BY c.customer_id
HAVING COUNT(*) = (
    SELECT COUNT(*)
    FROM Product
)