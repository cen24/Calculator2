from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from Database import create_model

engine = create_engine("sqlite:///db1.sqlite")
session = Session(bind=engine)

# Populate Customer Data
c1 = create_model.Customer(first_name='Toby',
                           last_name='Miller',
                           username='tmiller',
                           email='tmiller@example.com',
                           address='1662 Kinney Street',
                           town='Wolfden'
                           )

c2 = create_model.Customer(first_name='Scott',
                           last_name='Harvey',
                           username='scottharvey',
                           email='scottharvey@example.com',
                           address='424 Patterson Street',
                           town='Beckinsdale'
                           )

session.add(c1)
session.add(c2)
session.commit()

c3 = create_model.Customer(
                            first_name="John",
                            last_name="Lara",
                            username="johnlara",
                            email="johnlara@mail.com",
                            address="3073 Derek Drive",
                            town="Norfolk"
)

c4 = create_model.Customer(
                            first_name="Sarah",
                            last_name="Tomlin",
                            username="sarahtomlin",
                            email="sarahtomlin@mail.com",
                            address="3572 Poplar Avenue",
                            town="Norfolk"
)

c5 = create_model.Customer(first_name='Toby',
                           last_name='Miller',
                           username='tmiller',
                           email='tmiller@example.com',
                           address='1662 Kinney Street',
                           town='Wolfden'
                           )

c6 = create_model.Customer(first_name='Scott',
                           last_name='Harvey',
                           username='scottharvey',
                           email='scottharvey@example.com',
                           address='424 Patterson Street',
                           town='Beckinsdale'
                           )

session.add_all([c3, c4, c5, c6])
session.commit()