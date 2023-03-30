from flask import Flask, render_template#, request
# from elasticsearch import Elasticsearch

from uuid import uuid4
from string import printable
import random
import lorem
import datetime


app = Flask(__name__)
# es = Elasticsearch(hosts="http://localhost:9200")




PRINTABLE = [i for i in printable]

DOCUMENTS = [
    {
        "id": uuid4(),
        "number": "".join(random.choices(PRINTABLE, k=6)),
        "text": "<br><br>".join([lorem.text() for _ in range(10)]),
        "date": datetime.date.today(),
        "jurisdiction_name": "Cour d'appel de Paris"
    } for i in range(20)
]


@app.route("/", methods=["GET", "POST"])
def get_index():
    return render_template("index.html", documents=DOCUMENTS)

@app.route("/decision/<decision_id>", methods=["GET"])
def get_decision_id(decision_id):
    decision = DOCUMENTS[0]
    return render_template("decision.html", decision=decision)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)