import sqlite3

conn = sqlite3.connect('items.db', check_same_thread=False)

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS food (
           Fid INTEGER PRIMARY KEY,
           Ftype TEXT,
           amount INTEGER,
           place TEXT
           )""")

def insert_food(id, typ, amount, place):
    with conn:
        c.execute("INSERT INTO food VALUES (:Fid, :Ftype, :amount, :place)", {'Fid': id, 'Ftype': typ, 'amount': amount, 'place': place})

def update_food_amount(id, typ, operation):
    c.execute("SELECT amount FROM food WHERE Fid = :Fid AND Ftype = :Ftype", {'Fid': id, 'Ftype': typ})
    amount = c.fetchone()
    if amount[0] == 0:
        delete_food(id, typ)
        return amount[0]
    with conn:
        if operation:
            c.execute("""UPDATE food SET amount = :amount
                        WHERE Fid = :Fid AND Ftype = :Ftype""", {'Fid': id, 'Ftype': typ, 'amount': amount[0] + 1})
            return amount[0] + 1

        else:
            c.execute("""UPDATE food SET amount = :amount
                                    WHERE Fid = :Fid AND Ftype = :Ftype""", {'Fid': id, 'Ftype': typ, 'amount': amount[0] - 1})
            return amount[0] - 1

def get_all_food():
    arrayData = []
    c.execute("SELECT * FROM food")
    rows = c.fetchall()
    for row in rows:
        arrayData.append(row)
    arrayDictData = [{"id": item[0], "Typ": item[1], "Menge": item[2], "Ort": item[3]} for item in arrayData]
    return arrayDictData

def get_food(typ):
    c.execute("SELECT * FROM food WHERE Ftype = :Ftype", {'Ftype': typ})
    data = c.fetchone()
    dictData = [{"id": data[0], "Typ": data[1], "Menge": data[2], "Ort": data[3]}]
    return dictData

def delete_food(id, typ):
    with conn:
        c.execute("DELETE FROM food WHERE Fid = :Fid AND Ftype = :Ftype",
                  {'Fid': id, 'Ftype': typ})

def delete_all_food():
    with conn:
        c.execute("DELETE FROM food")
