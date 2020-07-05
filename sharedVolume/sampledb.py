import os
from conf import db
from pyschema import Fruit

# Data to initialize database with
FRUIT = {   
            3: {'mango': 5, 'orange': 6}, 
            1: {'mango': 2, 'orange': 7}, 
            4: {'mango': 0, 'orange': 11}
        }

# Delete database file if it exists currently
if os.path.exists("fruit.db"):
    os.remove("fruit.db")

# Create the database
db.create_all()

# iterate over the PEOPLE structure and populate the database
for date in list(FRUIT.keys()):
    f = Fruit(date=date,
                mango=FRUIT[date]['mango'],
                orange=FRUIT[date]['orange'],
    )
    db.session.add(f)

db.session.commit()
print(Fruit.__table__.columns)