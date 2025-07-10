from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    return "Hello World!"

@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json()
    return jsonify({"you_sent": data})

@app.route("/pokemon/<name>", methods=["GET"])
def proxy_pokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = requests.get(url)
    if response.status_code != 200:
        return jsonify({"error": "Pokémon not found"}), response.status_code
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)
