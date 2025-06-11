-- Write your PostgreSQL query statement below
SELECT p.firstname "firstName", p.lastname "lastName", city, state
FROM Person p LEFT JOIN Address a ON p.personId = a.personId