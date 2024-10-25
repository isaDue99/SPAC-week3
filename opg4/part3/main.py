# python MySQL northwind database exercise assignment

import sqlite3
import pandas as pd
from matplotlib import pyplot as plt

### 1. connect to northwind database
# cant connect to the mysql server and sqlite doesnt handle the northwind.sql file well = well use an equivalent database
database = "northwind.db"

con = sqlite3.connect(database)
cur = con.cursor()


### 2. use sql to gather data from the tables
queries = {
    "country sales" : "SELECT ShipCountry from Orders",
    # 2-3 further diagrams
    "customer countries" : "SELECT Country from Customers",
    "employee territories" : "SELECT * from EmployeeTerritories",
    "countries product category" : 
        "SELECT Orders.ShipCountry, Categories.CategoryName FROM ((Orders INNER JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID) INNER JOIN Products ON OrderDetails.ProductID = Products.ProductID) INNER JOIN Categories ON Products.CategoryID = Categories.CategoryID"
}

data = {}

for label, query in queries.items():
    #data[label] = cur.execute(query).fetchall()

    # load into pandas dataframes
    data[label] = pd.read_sql_query(query, con)

# close the database connection when were done with it
con.close()


### 3. use pandas to load and analyse the data. find sales for each country
country_sales = data["country sales"].value_counts()


### 4. use matplotlib to create a bar diagram that shows sales for each country
x_axis = [i[0] for i in country_sales.index]
y_axis = country_sales.to_numpy()

# make a bar plot
plt.figure("Sales by country")
fig = plt.bar(x=x_axis, height=y_axis)
# add the sales numbers to each bar
plt.bar_label(fig)
# rotate the country labels so they dont overlap
plt.tick_params(axis='x', labelrotation=90)
# add a title to diagram
plt.suptitle("Sales by country")


### 5. analyse data and create 2-3 further relevant diagrams based on the data

#    how many customers in each country?
# new figure
plt.figure("Sales to customers per country")

# we get more out of this diagram if we include the bars from the country sales plot too.
fig = plt.bar(x=x_axis, height=y_axis)
plt.bar_label(fig)

# now we get customer per country data
customer_countries = data["customer countries"].value_counts()

x_axis = [i[0] for i in customer_countries.index]
y_axis = customer_countries.to_numpy()

# make a bar plot like before
fig = plt.bar(x=x_axis, height=y_axis)
plt.bar_label(fig)
plt.tick_params(axis='x', labelrotation=90)
plt.suptitle("Sales to customers per country")


#   how many territories does each employee manage?
plt.figure("Employee territories")

employee_territories = data["employee territories"]["EmployeeID"].value_counts()

labels = ["Employee " + str(x) for x in employee_territories.index]
plt.pie(employee_territories, labels=labels, autopct='%1.1f%%', pctdistance=1.15, labeldistance=.3, rotatelabels=True, startangle=90)
plt.suptitle("Amount of territories managed by each employee")


#   Favorite product category across countries? (this one might be too much for the time left)
#plt.figure("Product categories popularity")

category_popularity = data["countries product category"]

cat_pop = category_popularity.value_counts()

res = {}
for i in range(len(cat_pop)):
    country, category = cat_pop.index[i]
    count = cat_pop[i]
    try:
        res[country] = res[country] + f", {category} : {count}"
    except:
        res[country] = f"{category} : {count}"

print("\n### Favored product categories by country ###\n")
for country, str in res.items():
    print(f"{country} :\n   {str}\n")


# the vision: stacked bars/pies for each country, slices of bars/pies is the categories that country has bought products from
# HOWEVER not much time left...


# actually show the figure we made
plt.show()