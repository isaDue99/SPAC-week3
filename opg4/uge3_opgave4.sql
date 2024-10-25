# SQL exercise asssignment

# 1. Make ER Diagram of Northwind Database
# Done

# 2. List all products from products, sorted descending by UnitPrice
# (Should return 77)
select * from products order by UnitPrice desc;

# 3. Find all customers from the UK and Spain
# (Should return 12 rows)
select * from customers where Country = "UK" or Country = "Spain";

# 4. Find all products that have more than 100 units in stock, and where unit price is more or equal to 25
# (Should return 10 rows - ERROR, less than 10?)
select * from products where UnitsInStock > 100 and UnitPrice >= 25;

# 5. Find all countries that an order has been sent to, show them only once
# (Should return 21 rows)
select distinct ShipCountry from orders;

# 6. Find all orders placed in the 10th month of 1996
# (Should return 26 rows)
select * from orders where month(OrderDate) = 10 and year(OrderDate) = 1996;

# 7. Find all orders where ShipRegion is blank, ShipCountry = Germany, Freight is >= 100, EmployeeID = 1, and OrderDate is from 1996
# (Should return 2 rows)
select * from orders where isnull(ShipRegion) = true and ShipCountry = "Germany" and Freight >= 100 and EmployeeID = 1 and year(OrderDate) = 1996;

# 8. Find orders not shipped on time: ShippedDate great than RequiredDate
# (Should return 37 rows)
select * from orders where ShippedDate > RequiredDate;

# 9. Find all orders from january, february, march or april in 1997 destined for Canada
# (Should return 8 rows)
select * from orders where year(OrderDate) = 1997 and month(OrderDate) between 1 and 4 and ShipCountry = "Canada";

# 10. Find the orders where EmployeeID is either 2, 5, or 8, ShipRegion isn't blank, and ShipVia is either 1 or 3. Sort first by EmployeeID, then ShipVia, both ascending
# (Should return 57 rows)
select * from orders where EmployeeID in (2, 5, 8) and isnull(ShipRegion) = false and ShipVia in (1, 3)
order by EmployeeID asc, ShipVia asc;

# 11. Find the employees with no value in Region or ReportsTo is blank. They should also be born in 1960 or earlier. - ERROR, ReportsTo doesnt exist
# (Should return 3 rows - but error might change that)
select * from employees where isnull(Region) = true and year(BirthDate) <= 1960;