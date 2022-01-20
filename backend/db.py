import sqlite3

conn = sqlite3.connect('items.db', check_same_thread=False)

c = conn.cursor()



def insert_food(typ, amount, place):
    c.execute("""CREATE TABLE IF NOT EXISTS food (
               Ftype TEXT,
               amount INTEGER,
               place TEXT,
               PRIMARY KEY (Ftype, place)
               )""")
    with conn:
        c.execute("INSERT INTO food VALUES (:Ftype, :amount, :place)", {'Ftype': typ, 'amount': amount, 'place': place})

def update_food_amount(typ, operation):
    c.execute("SELECT amount FROM food WHERE Ftype = :Ftype", {'Ftype': typ})
    amount = c.fetchone()
    if amount[0] - 1 == 0:
        delete_food(typ)
        return amount[0] - 1
    with conn:
        if operation:
            c.execute("""UPDATE food SET amount = :amount
                        WHERE Ftype = :Ftype""", {'Ftype': typ, 'amount': amount[0] + 1})
            return amount[0]  + 1

        else:
            c.execute("""UPDATE food SET amount = :amount
                                    WHERE Ftype = :Ftype""", {'Ftype': typ, 'amount': amount[0] - 1})
            return amount[0] - 1

def get_all_food():
    arrayData = []
    c.execute("SELECT * FROM food")
    rows = c.fetchall()
    for row in rows:
        arrayData.append(row)
    arrayDictData = [{"Typ": item[0], "Menge": item[1], "Ort": item[2]} for item in arrayData]
    return arrayDictData

def get_food(typ):
    c.execute("SELECT * FROM food WHERE Ftype = :Ftype", {'Ftype': typ})
    data = c.fetchone()
    dictData = [{"Typ": data[0], "Menge": data[1], "Ort": data[2]}]
    return dictData

def delete_food(typ):
    with conn:
        c.execute("DELETE FROM food WHERE Ftype = :Ftype",
                  {'Ftype': typ})

def delete_all_food():
    with conn:
        c.execute("DELETE FROM food")
