select name
from SalesPerson
where Sales_id 
not in(select Sales_id from Orders
 where com_id=(select com_id from Company where name ='RED'))
