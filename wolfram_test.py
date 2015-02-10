# -*- coding: utf-8 -*-
from flask import Flask, make_response
from json import dumps
import pytest
import wolframalpha

app_id = "4J8QQ4-YK54UPKG83"

app = Flask(__name__)

@app.route("/")
def index():
	return "Wolfram test"

@app.route("/<question>")
def get_answer(question):
	hola = search_wolframalpha(question)
	return make_response(dumps(hola, ensure_ascii=False).encode("utf-8"))
	

def search_wolframalpha(question):
	cliente = wolframalpha.Client(app_id)
	res = cliente.query(question)
	if len(res.pods) > 0:
		results = list(res.results)
		return results[0].text
	else:
		return "No tengo respuesta para eso"

if __name__ == "__main__":
	app.run()