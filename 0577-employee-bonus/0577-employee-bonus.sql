# Write your MySQL query statement below
select Employee.name , Bonus.Bonus
from Employee LEFT OUTER JOIN 
Bonus ON Employee.empid = Bonus.empid
WHERE bonus < 1000 OR bonus is NULL ;