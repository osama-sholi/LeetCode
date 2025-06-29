-- Write your PostgreSQL query statement below
SELECT p1.product_id, COALESCE(p2.new_price,10) price
FROM
(
    SELECT DISTINCT ON(product_id) product_id
    FROM Products
) p1
LEFT JOIN
(
    SELECT DISTINCT ON(product_id) *
    FROM Products
    WHERE change_date <= '2019-08-16'
    ORDER BY product_id, change_date DESC
) p2 ON p1.product_id = p2.product_id