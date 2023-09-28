from flask import Flask, request, render_template, jsonify
import os
import pandas as pd
from datetime import datetime
import pymongo

# Esta parte no está terminada porque al final no pude reunirme con nadie de FullStack para concretar inputs y returns de las funciones.

MONGO_URI='mongodb+srv://desafio2023:KKOUiQoxhsXLZZbL@desafio2023.zxi6fa6.mongodb.net/desafio2023'

myclient = pymongo.MongoClient(MONGO_URI)

os.environ['REPLICATE_API_TOKEN'] = "r8_3Cn377wOsZ8ywqtFyCCicG5JwHqpHYS0sONIW"
engine = create_engine('postgresql://fl0user:ClU4ueygKz9G@ep-red-butterfly-89282058.eu-central-1.aws.neon.tech:5432/spaces?sslmode=require')
db = myclient["desafio2023"]
calendar_id = "AAMkAGIxMWE3N2ZmLWU5NTYtNDk3Zi1iOTkwLTg2ZDJjNDBmNzQxYwBGAAAAAAB80dAJyo36SYoYzkanvIWzBwBlRyW6AVWKQ4jOeYRcLxqXAAAAAAEGAABlRyW6AVWKQ4jOeYRcLxqXAABUbHJkAAA="

app = Flask(__name__)

@app.route("/calendario", methods=["GET"])
def calendar():

    url = r'https://outlook.office365.com/owa/calendar/b11a77ffe956497fb99086d2c40f741c@edem.es/e09257c6f9e944f1bf4bbd05ccff08123080417746668936894/calendar.html'
    return jsonify({"calendario": url})


@app.route("/create_event", methods=["POST"])
def cre_event():
        # Step 2.1 Create an event


    # uri de la base de datos

    questions = db["questions"]
    orders = db["orders"]
    reviews = db["reviews"]
    events = db["events"]
    users = db["users"]

    def construct_event_detail(event_name, **event_details):
        # En esta función tiene que entrar la info del evento, 
        # y devolver un diccionario con la info del evento
        # más abajo hay un ejemplo.
        request_body = {
            'subject': event_name
        }
        for key, val in event_details.items():
            request_body[key] = val
        return request_body
    

    # id del calendario, si se crea uno nuevo, hay que cambiarlo

    response1_create = requests.post(
        GRAPH_API_ENDPOINT + f'/me/calendars/{calendar_id}/events',
        headers=headers,
        json=construct_event_detail(f'{event_name}')
    )
    console.print(response1_create.json()) # Evento generado correctamente

@app.route("/delete_event", methods=["DELETE"])
def del_event():
    pass

@app.route("/mod_event", methods=["PATCH"])
def mod_event():
    pass

@app.route("/delete_event", methods=["POST"])
def del_event():
    pass

if __name__=="__main__":
    app.run(debug=True, port=8000)