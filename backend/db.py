import sqlite3

conn = sqlite3.connect('items.db', check_same_thread=False)
c = conn.cursor()


def insert_food(typ, amount, place, comment):
    c.execute("""CREATE TABLE IF NOT EXISTS food (
               Ftype TEXT,
               amount INTEGER,
               place TEXT,
               comment TEXT,
               PRIMARY KEY (Ftype, place)
               )""")
    with conn:
        c.execute("INSERT INTO food VALUES (:Ftype, :amount, :place, :comment)", {'Ftype': typ, 'amount': amount, 'place': place, 'comment': comment})


def update_food_amount(typ, amount, place):
    c.execute("""UPDATE food SET amount = :amount
                WHERE Ftype = :Ftype AND place = :place""", {'Ftype': typ, 'amount': amount, 'place': place})
    return amount


def update_food_comment(typ, place, comment):
    c.execute("""UPDATE food SET comment = :comment
                WHERE Ftype = :Ftype AND place = :place""", {'Ftype': typ, 'place': place, 'comment': comment})


def get_all_food():
    arrayData = []
    c.execute("SELECT * FROM food")
    rows = c.fetchall()
    for row in rows:
        arrayData.append(row)
    arrayDictData = [{"Typ": item[0], "Menge": item[1], "Ort": item[2], "Kommentar": item[3]} for item in arrayData]
    return arrayDictData


def get_food(typ):
    c.execute("SELECT * FROM food WHERE Ftype = :Ftype", {'Ftype': typ})
    data = c.fetchone()
    dictData = [{"Typ": data[0], "Menge": data[1], "Ort": data[2]}]
    return dictData


def delete_food(typ, place):
    with conn:
        c.execute("DELETE FROM food WHERE Ftype = :Ftype AND place = :place",
                  {'Ftype': typ, 'place': place})


def delete_comment(typ, place):
    with conn:
        c.execute("UPDATE food SET comment=NULL WHERE Ftype = :Ftype AND place = :place",
                  {'Ftype': typ, 'place': place})


def delete_all_food():
    with conn:
        c.execute("DELETE FROM food")
