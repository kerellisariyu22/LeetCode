#select name
#from SalesPerson
#where Sales_id 
#not in(select Sales_id from Orders
 #where com_id=(select com_id from Company where name ='RED'))


select s.name 
from salesperson as s left join orders as o 
on s.sales_id = o.sales_id
left join company as c on o.com_id = c.com_id
group by s.name
having sum(c.name = 'RED') = 0
or sum(c.name = 'RED') is NULL ;