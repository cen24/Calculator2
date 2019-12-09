from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from Database import sqlite_create

engine = create_engine("sqlite:///db1.sqlite")
session = Session(bind=engine)


c1 = sqlite_create.Customer(first_name='Toby',
                           last_name='Miller',
                           username='tmiller',
                           email='tmiller@example.com',
                           address='1662 Kinney Street',
                           town='Wolfden'
                           )

c2 = sqlite_create.Customer(first_name='Scott',
                           last_name='Harvey',
                           username='scottharvey',
                           email='scottharvey@example.com',
                           address='424 Patterson Street',
                           town='Beckinsdale'
                           )

session.add(c1)
session.add(c2)
session.commit()

c3 = sqlite_create.Customer(
                            first_name="John",
                            last_name="Lara",
                            username="johnlara",
                            email="johnlara@mail.com",
                            address="3073 Derek Drive",
                            town="Norfolk"
)

c4 = sqlite_create.Customer(
                            first_name="Sarah",
                            last_name="Tomlin",
                            username="sarahtomlin",
                            email="sarahtomlin@mail.com",
                            address="3572 Poplar Avenue",
                            town="Norfolk"
)

c5 = sqlite_create.Customer(first_name='Toby',
                           last_name='Miller',
                           username='tmiller',
                           email='tmiller@example.com',
                           address='1662 Kinney Street',
                           town='Wolfden'
                           )

c6 = sqlite_create.Customer(first_name='Scott',
                           last_name='Harvey',
                           username='scottharvey',
                           email='scottharvey@example.com',
                           address='424 Patterson Street',
                           town='Beckinsdale'
                           )

session.add_all([c3, c4, c5, c6])
session.commit()

# Adding Items
i1 = sqlite_create.Item(name='Chair', cost_price=9.21, selling_price=10.81, quantity=5)
i2 = sqlite_create.Item(name='Pen', cost_price=3.45, selling_price=4.51, quantity=3)
i3 = sqlite_create.Item(name='Headphone', cost_price=15.52, selling_price=16.81, quantity=50)
i4 = sqlite_create.Item(name='Travel Bag', cost_price=20.1, selling_price=24.21, quantity=50)
i5 = sqlite_create.Item(name='Keyboard', cost_price=20.1, selling_price=22.11, quantity=50)
i6 = sqlite_create.Item(name='Monitor', cost_price=200.14, selling_price=212.89, quantity=50)
i7 = sqlite_create.Item(name='Watch', cost_price=100.58, selling_price=104.41, quantity=50)
i8 = sqlite_create.Item(name='Water Bottle', cost_price=20.89, selling_price=25, quantity=50)

session.add_all([i1, i2, i3, i4, i5, i6, i7, i8])
session.commit()

# Adding Orders
o1 = sqlite_create.Order(customer=c1)
o2 = sqlite_create.Order(customer=c1)

line_item1 = sqlite_create.OrderLine(order=o1, item=i1, quantity=3)
line_item2 = sqlite_create.OrderLine(order=o1, item=i2, quantity=2)
line_item3 = sqlite_create.OrderLine(order=o2, item=i1, quantity=1)
line_item3 = sqlite_create.OrderLine(order=o2, item=i2, quantity=4)

session.add_all([o1, o2])

session.new
session.commit()

o3 = sqlite_create.Order(customer=c1)
order_line1 = sqlite_create.OrderLine(order=o1, item=i1, quantity=5)
order_line2 = sqlite_create.OrderLine(order=o1, item=i2, quantity=10)

session.add_all([o3])

session.commit()