# Write your MySQL query statement below
SELECT A.name as Employee FROM Employee A, Employee B WHERE A.salary > B.salary and A.managerId = B.id
