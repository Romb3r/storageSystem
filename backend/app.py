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
    db.insert_food(typ, amount, place, "")
    return {"Typ": typ, "Menge": amount, "Ort": place}


@app.put("/update/food/{typ}/{place}/{amount}")
def update_food_amount(typ: str, place: str, amount: int):
    amount = db.update_food_amount(typ, amount, place)
    if amount == 0:
        db.delete_food(typ, place)
        return {"Typ": typ, "Ort": place, "Status": "deleted"}
    return {"Typ": typ, "Ort": place, "Neue Menge": amount}


@app.put("/update/comment/{typ}/{place}/{comment}")
def update_food_comment(typ: str, place: str, comment: str):
    db.update_food_comment(typ, place, comment)
    return {"Typ": typ, "Ort": place, "Neuer Kommentar": comment}


@app.delete("/delete/food/{typ}/{place}")
def delete_food(typ: str, place: str):
    db.delete_food(typ, place)
    return {"Typ": typ, "Ort": place, "Status": "deleted"}


@app.delete("/delete/comment/{typ}/{place}")
def delete_comment(typ: str, place: str):
    db.delete_comment(typ, place)
    return {"Typ": typ, "Ort": place, "Kommentar": "deleted"}


@app.delete("/delete/all/food")
def delete_all_food():
    db.delete_all_food()
    return {"Status": "all deleted"}
