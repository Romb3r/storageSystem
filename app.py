from fastapi import FastAPI
import db

app = FastAPI()

@app.get("/")
def print_service():
    return "Lebensmittel Bestand"

@app.get("/get/all/food")
def get_all_food():
    return db.get_all_food()

@app.get("/get/food/{typ}")
def get_food(typ: str):
    return db.get_food(typ)

@app.post("/insert/food/{id}/{typ}/{amount}/{place}")
def insert_food(id: int, typ: str, amount: int, place: str):
    db.insert_food(id, typ, amount, place)
    return {"id": id, "Typ": typ, "Menge": amount, "Ort": place}

@app.put("/update/food/{id}/{typ}/{operation}")
def update_food_amount(id: int, typ: str, operation: bool):
    amount = db.update_food_amount(id, typ, operation)
    return {"id": id, "Typ": typ, "Neue Menge": amount}

@app.delete("/delete/food/{id}/{typ}")
def delete_food(id: int, typ: str):
    db.delete_food(id, typ)
    return {"id": id, "Typ": typ, "Status": "deleted"}

@app.delete("/delete/all/food")
def delete_all_food():
    db.delete_all_food()
    return {"Status": "all deleted"}
