# Write your MySQL query statement below
SELECT name as Customers FROM Customers WHERE id NOT IN (SELECT Customers.id FROM Customers JOIN Orders WHERE Customers.id = customerId)
