#-*- coding: utf-8 -*-
from flask import Flask, make_response
from json import dumps
import pytest
import wolframalpha

app_id = "4J8QQ4-YK54UPKG83"

app = Flask(__name__)

@app.route("/ask/<question>")
def test_basic(question):
	cliente = wolframalpha.Client(app_id)
	#res = cliente.query('who is brasil president')
	res = cliente.query('capital of peru')
	if len(res.pods) > 0:
		results = list(res.results)
		#for result in results:
		#	print result.text
		return results[0].text
	else:
		return "No tengo respuesta para eso"

if __name__ == "__main__":
	app.run()