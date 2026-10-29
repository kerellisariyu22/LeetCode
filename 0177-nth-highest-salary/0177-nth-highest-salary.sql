CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET N=N-1;
  RETURN (
     select DISTINCT salary
     from employee
     ORDER BY salary DESC
     LIMIT 1 OFFSET N 

  );
END