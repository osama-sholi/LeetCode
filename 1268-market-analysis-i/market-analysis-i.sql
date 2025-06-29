-- Write your PostgreSQL query statement below
SELECT u.user_id buyer_id, u.join_date, COALESCE(COUNT(order_date),0) orders_in_2019
FROM Users u LEFT JOIN (
    SELECT *
    FROM Orders
    WHERE EXTRACT(YEAR FROM order_date) = '2019'
) o ON u.user_id = o.buyer_id
GROUP BY u.user_id, u.join_date