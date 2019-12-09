
import datetime

from sqlalchemy import *
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from Database import sqlite_create

engine = create_engine("sqlite:///db1.sqlite")
session = Session(bind=engine)

print("=========Customers=========")
# prints all the records of  the Customers table
result = session.query(sqlite_create.Customer).all()
for row in result:
    print("Name: ", row.first_name, " ", row.last_name, " Address:", row.address, " Email:", row.email)
print("===========================")

print("=========Item=========")
# prints all the records of  the Item table
result = session.query(sqlite_create.Item).all()
for row in result:
    print("Name: ", row.name, " Cost Price:", row.cost_price, " Selling Price:", row.selling_price, " Quantity:",
          row.quantity)
print("===========================")

print("=========Orders=========")
# prints all the records of  the Order table
result = session.query(sqlite_create.Order).all()
for row in result:
    print("ID: ", row.id, " Date Placed:", row.date_placed, " Customer Id:", row.customer_id)
print("===========================")

print("=========SQL Query for Customer=========")
print(session.query(sqlite_create.Customer))
print("===========================")

print("=========count()=========")
print(session.query(sqlite_create.Customer).count())  # get the total number of records in the customers table
print(session.query(sqlite_create.Item).count())  # get the total number of records in the items table
print(session.query(sqlite_create.Order).count())  # get the total number of records in the orders table
print("===========================")

print("=========first()=========")
result = session.query(sqlite_create.Customer).first()
print("Name: ", result.first_name, " ", result.last_name, " Address:", result.address, " Email:", result.email)

result = session.query(sqlite_create.Item).first()
print("Name: ", result.name, " Cost Price:", result.cost_price, " Selling Price:", result.selling_price, " Quantity:",
      result.quantity)

result = session.query(sqlite_create.Order).first()
print("ID: ", result.id, " Date Placed:", result.date_placed, " Customer Id:", result.customer_id)
print("===========================")

print("=========get()=========")
result = session.query(sqlite_create.Customer).get(1)
print("Name: ", result.first_name, " ", result.last_name, " Address:", result.address, " Email:", result.email)
result = session.query(sqlite_create.Item).get(1)
print("Name: ", result.name, " Cost Price:", result.cost_price, " Selling Price:", result.selling_price, " Quantity:",
      result.quantity)
result = session.query(sqlite_create.Order).get(100)
if result is not None:
    print("ID: ", result.id, " Date Placed:", result.date_placed, " Customer Id:", result.customer_id)
else:
    print(result)
print("===========================")

print("=========filter()=========")
result = session.query(sqlite_create.Customer).filter(sqlite_create.Customer.first_name == 'John').all()
print("\n~~All customers with name starting with John:~~")
for row in result:
    print("Name: ", row.first_name, " ", row.last_name, " Address:", row.address, " Email:", row.email)

result = session.query(csqlite_create.Customer).filter(sqlite_create.Customer.id <= 5,
                                                     sqlite_create.Customer.town.like("Nor%")).all()
print("\n~~All customers with id less than or equal to 5 and living in Norfolk town:~~")
for row in result:
    print("Name: ", row.first_name, " ", row.last_name, " Address:", row.address, " Email:", row.email)

print("\n~~find all customers who either live in Peterbrugh or Norfolk~~")
result = session.query(sqlite_create.Customer).filter(
    or_(sqlite_create.Customer.town == 'Peterbrugh', sqlite_create.Customer.town == 'Norfolk')).all()
for row in result:
    print("Name: ", row.first_name, " ", row.last_name, " Address:", row.address, " Email:", row.email)

print("\n~~find all customers whose first name is John and live in Norfolk~~")
result = session.query(sqlite_create.Customer).filter(
    and_(sqlite_create.Customer.first_name == 'John', sqlite_create.Customer.town == 'Norfolk')).all()
for row in result:
    print("Name: ", row.first_name, " ", row.last_name, " Address:", row.address, " Email:", row.email)

print("\n~~find all johns who don't live in Peterbrugh~~")
result = session.query(sqlite_create.Customer).filter(
    and_(sqlite_create.Customer.first_name == 'John', not_(sqlite_create.Customer.town == 'Peterbrugh', ))).all()
for row in result:
    print("Name: ", row.first_name, " ", row.last_name, " Address:", row.address, " Email:", row.email)
print("===========================")
print("\n")

print("=========filter() with NOT, NULL, IN, BETWEEN=========")
result = session.query(sqlite_create.Order).filter(sqlite_create.Order.date_placed == None).all()
print("\n~~All Orders with Date Shipped as None:~~")
if result is not None:
    for row in result:
        print("ID: ", row.id, " Date Placed:", row.date_placed, " Customer Id:", row.customer_id)
else:
    print("NO RESULT")

result = session.query(sqlite_create.Order).filter(sqlite_create.Order.date_placed != None).all()
print("\n~~All Orders with Date Shipped Not as None:~~")
if result is not None:
    for row in result:
        print("ID: ", row.id, " Date Placed:", row.date_placed, " Customer Id:", row.customer_id)
else:
    print("NO RESULT")

result = session.query(sqlite_create.Item).filter(sqlite_create.Item.cost_price.between(10, 50)).all()
print("\n~~All Items whose cost price is between 10 and 50:~~")
for row in result:
    print("Name: ", row.name, " Cost Price:", row.cost_price, " Selling Price:", row.selling_price, " Quantity:",
          row.quantity)

result = session.query(sqlite_create.Item).filter(sqlite_create.Item.cost_price.between(10, 50)).all()
print("\n~~All Items whose cost price is not between 10 and 50:~~")
for row in result:
    print("Name: ", row.name, " Cost Price:", row.cost_price, " Selling Price:", row.selling_price, " Quantity:",
          row.quantity)

result = session.query(sqlite_create.Item).filter(sqlite_create.Item.name.like("%r")).all()
print("\n~~All Items whose name ends with r:~~")
for row in result:
    print("Name: ", row.name, " Cost Price:", row.cost_price, " Selling Price:", row.selling_price, " Quantity:",
          row.quantity)

result = session.query(sqlite_create.Item).filter(sqlite_create.Item.name.like("w%")).all()
print("\n~~All Items whose name starts with w:~~")
for row in result:
    print("Name: ", row.name, " Cost Price:", row.cost_price, " Selling Price:", row.selling_price, " Quantity:",
          row.quantity)
print("===========================")

print("=========limit()=========")
result = session.query(sqlite_create.Customer).limit(2).all()
print("~~Printing all customers but limiting to 2:~~")
for row in result:
    print("Name: ", row.first_name, " ", row.last_name, " Address:", row.address, " Email:", row.email)
print("===========================")

print("=========offset()=========")
result = session.query(sqlite_create.Customer).limit(2).offset(2).all()
print("~~Printing all customers but limiting to 2 and offsetting to 2:~~")
for row in result:
    print("Name: ", row.first_name, " ", row.last_name, " Address:", row.address, " Email:", row.email)
print("===========================")

print("=========order_by()=========")
result = session.query(sqlite_create.Item).filter(sqlite_create.Item.name.like("wa%")).order_by(
    desc(sqlite_create.Item.cost_price)).all()
print("~~Printing all items that start with wa and then it is sorted by the cost price in descending order:~~")
for row in result:
    print("Name: ", row.name, " Cost Price:", row.cost_price, " Selling Price:", row.selling_price, " Quantity:",
          row.quantity)
print("===========================")

print("\n=========join()=========")
result = session.query(sqlite_create.Customer, sqlite_create.Order.date_placed).join(sqlite_create.Order).all()
print("~~Join between Customer and Order:~~")
for row in result:
    print(" Order placed on:", row.date_placed)
print("===========================")

print("\n=========outerjoin()=========")
result = session.query(sqlite_create.Customer.first_name, sqlite_create.Order.id).outerjoin(sqlite_create.Order).all()
print("~~Outer Join between Customer and Order:~~")
for row in result:
    print(" Order placed by:", row.first_name, " with Order ID:", row.id)
print("===========================")

print("\n=========groupby()=========")
result = session.query(func.count(sqlite_create.Customer.id)).join(sqlite_create.Order).filter(
    sqlite_create.Customer.first_name == 'John',
    sqlite_create.Customer.last_name == 'Green',
).group_by(sqlite_create.Customer.id).scalar()
print("~~Number of Orders made by John Green:~~")
print(result)
print("===========================")

print("\n=========Dealing with Duplicates=========")
result = session.query(sqlite_create.Customer.town).filter(sqlite_create.Customer.id <= 10).distinct().all()
print("~~Distinct towns:~~")

for row in result:
    print(row.town)
print("===========================")

print("\n=========Union=========")
s1 = session.query(sqlite_create.Item.id, sqlite_create.Item.name).filter(sqlite_create.Item.name.like("Wa%"))
s2 = session.query(sqlite_create.Item.id, sqlite_create.Item.name).filter(sqlite_create.Item.name.like("%e%"))
result = s1.union(s2).all()
print("~~Union between items starting with Wa and having a e in between:~~")

for row in result:
    print(row)
print("===========================")

print("\n=========Updating Data=========")
result = session.query(sqlite_create.Item).filter(
    sqlite_create.Item.name.ilike("W%")
).update({"quantity": 60}, synchronize_session='fetch')
session.commit()
print("~~Updating  Item starting with W:~~")

print(result)
print("===========================")

print("\n=========Deleting Data=========")
result = session.query(sqlite_create.Item).filter(sqlite_create.Item.name == 'Monitor').one()
session.delete(result)
session.commit()
print("~~Deleting Item Monitor:~~")

print(result.name)
print("===========================")

print("\n=========Transactions=========")
result = session.query(sqlite_create.Order).all()

print("~~Orders Status:~~")


def dispatch_order(order_id):
    # check whether order_id is valid or not
    order = session.query(sqlite_create.Order).get(order_id)

    try:
        if not order:
            raise ValueError("Invalid order id: {}.".format(order_id))
    except ValueError as e:
        print(e)
        return

    try:
        if order.date_shipped:
            print("Order already shipped.")
            return
    except:
        pass

    try:
        for i in order.line_items:
            i.item.quantity = i.item.quantity - i.quantity

        order.date_shipped = datetime.now()
        session.commit()
        print("Transaction completed.")

    except IntegrityError as e:
        print(e)
        print("Rolling back ...")
        session.rollback()
        print("Transaction failed.")


print("~~Orders Status For Order ID 1:~~")
dispatch_order(1)
print("~~Orders Status For Order ID 2:~~")
dispatch_order(2)
print("~~Orders Status For Order ID 3:~~")
dispatch_order(3)
print("~~Orders Status For Order ID 4:~~")
dispatch_order(4)
print("===========================")