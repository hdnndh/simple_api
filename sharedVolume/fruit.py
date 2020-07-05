from datetime import datetime
from flask import make_response, abort
from conf import db, sqlite_url, conn
from pyschema import Fruit, fruitSchema, FRUIT_LIST
from sqlalchemy.inspection import inspect
import json
import sqlite3 


def add_column( column_name, data_type, database_name="fruit.db", table_name="fruit"):

    
    cursor = conn.cursor()

    if data_type == "integer":
        data_type_formatted = "INTEGER"
    elif data_type == "string":
        data_type_formatted = "VARCHAR(100)"

    base_command = ("ALTER TABLE '{table_name}' ADD column '{column_name}' '{data_type}'")
    sql_command = base_command.format(table_name=table_name, column_name=column_name, data_type=data_type_formatted)

    cursor.execute(sql_command)
    connection.commit()


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data to serve with our API
FRUIT = {
}

# Create a handler for our read (GET) people
def get(**kwargs):

    # Create the list of people from our data
    try:
        _from = kwargs.get('from', None)
        _to = kwargs.get('to', None)
        if _to < _from:
            raise ValueError('invalid range')
        print ("%s == %s" %(_from, _to)) 
        if (_from != None) and (_to != None):
            data = {}
            fruits = Fruit.query.filter(Fruit.date >= _from).filter(Fruit.date <= _to)
            schema = fruitSchema(many=True)
            dat = schema.dump(fruits)
            return dat
            # for date in range(int(_from), int(_to)+1):
            #     if date not in FRUIT.keys():
            #         continue
            #     for x in list(FRUIT[date].keys()):
            #         if x not in list(data.keys()):
            #             data[x] = int(FRUIT[date][x])
            #         else:
            #             data[x] += int(FRUIT[date][x])
            # return data
        else:
            raise ValueError('required from and to')
        
    except Exception as e:
        print(str(e))
        abort(406, str(e),)


def post(entry):
    try:
        date = int(entry.get("date", None))
        fruits = entry.get("fruits", None)
        for x in list(fruits.keys()):
            if x not in FRUIT_LIST:
                raise ValueError('invalid entry' + str(x))
        existing_entry = (
            Fruit.query.filter(Fruit.date == date)
            .one_or_none()
        )
        print("existing entry", existing_entry)
        if existing_entry is None:
            # schema = fruitSchema()
            new_entry = Fruit(date=date,
                                mango=fruits['mango'],
                                orange=fruits['orange']
            )
            db.session.add(new_entry)
            db.session.commit()
            # e_keys = conn.execute(que).keys()
            # print(conn.execute(query).keys())
            # for key in list(fruits.keys()):
            #     if key not in e_keys:
            #         add_column(column_name=key, data_type="integer")
            # which = (
            #     Fruit.query.filter(Fruit.date == date)
            #     .first()
            # )
            # for key in list(fruits.keys()): 
            #     setattr(which, key, fruits[key])

        else:
            raise ValueError('entry already exists')
        """
        reserved no db option
        """
        # if date not in FRUIT and date is not None:
        #     FRUIT[date] = fruits
        # else:
        #     raise ValueError('entry already exists')
        """
        reserved for put/update
        """
        # elif date is not None:
        #     for x in list(fruits.keys()):
        #         if x not in list(FRUIT[date].keys()):
        #             FRUIT[date][x] = int(fruits[x])
        #         else:
        #             FRUIT[date][x] += int(fruits[x])
        print(FRUIT)
        return make_response("done", 201)
    except Exception as e:
        print(str(e))
        abort(406, str(e),)
