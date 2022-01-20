from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import db, codecs

app = FastAPI()

def generate_html_res():
    html_content = codecs.open("../frontend/index.html", "r", encoding="utf-8")
    return HTMLResponse(content=html_content.read(), status_code=200)

@app.get("/index.html", response_class=HTMLResponse)
def print_service():
    return generate_html_res()

@app.get("/get/all/food")
def get_all_food():
    return db.get_all_food()

@app.get("/get/food/{typ}")
def get_food(typ: str):
    return db.get_food(typ)

@app.post("/insert/food/{typ}/{amount}/{place}")
def insert_food(typ: str, amount: int, place: str):
    db.insert_food(typ, amount, place)
    return {"Typ": typ, "Menge": amount, "Ort": place}

@app.put("/update/food/{typ}/{operation}")
def update_food_amount(typ: str, operation: bool):
    amount = db.update_food_amount(typ, operation)
    if amount == 0:
        return {"Typ": typ, "Status": "deleted"}
    return {"Typ": typ, "Neue Menge": amount}

@app.delete("/delete/food/{typ}")
def delete_food(typ: str):
    db.delete_food(typ)
    return {"Typ": typ, "Status": "deleted"}

@app.delete("/delete/all/food")
def delete_all_food():
    db.delete_all_food()
    return {"Status": "all deleted"}
