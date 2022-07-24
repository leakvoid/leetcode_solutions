CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      SELECT salary FROM (SELECT salary, ROW_NUMBER() OVER (ORDER BY salary DESC) AS rowNumber FROM Employee GROUP BY salary) AS tmp WHERE rowNumber = N
  );
END
