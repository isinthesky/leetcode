# Write your MySQL query statement below
select P.firstName, P.lastName, A.city, A.state
FROM Person P
LEFT JOIN Address A USING (personId)