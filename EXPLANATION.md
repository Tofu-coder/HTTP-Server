# HTTP Server Made by Dummies — From Omer

> This is a full walkthrough of the assignment — what I did, why I did it, and what I learned — explained like I’m explaining it to someone who likes clean coffee and clean code.

---

##  What Did I Build?

I built a real, working **HTTP server** using a Python library called **Flask**.

It runs on my machine at `http://127.0.0.1:5000` and it:

1. Says `"Hello World!"` when you visit `/`
2. Accepts and responds to **POST** requests at `/echo`
3. Fetches live Pokémon data from the internet (PokeAPI) at `/pokemon/<name>`

So, yes — this is a local API server, written by hand, from scratch. Huh, wasn't expecting myself to do this...

---

##  Step-by-Step Code Setup (With Dummy-Friendly Explanations)

###  1. Create a project folder

```bash
mkdir flask_http_server
cd flask_http_server
```

🗒️ _This is just the folder that holds everything I build._

---

###  2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

🗒️ _This creates a clean Python space so I don't mess up my global packages._

---

### � 3. Install Flask and Requests

```bash
pip install flask requests
```

🗒️ _Flask = the server framework. Requests = lets me make internet calls (like to the PokeAPI)._

---

###  4. Create `app.py` (The Actual Server Code)

```python
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
```

🗒️ _This file defines the server, its routes (URLs), and what each one does._

---

###  5. Create `requirements.txt`

```bash
echo -e "flask\nrequests" > requirements.txt
```

🗒️ _This lists the libraries needed to run the server._

---

###  6. Run the server

```bash
python app.py
```

🗒️ _Now the server is listening at `http://127.0.0.1:5000`._

---

###  7. Test it with `curl` (From Another Terminal)

####  `GET /`

```bash
curl http://127.0.0.1:5000/
```
Returns:
```
Hello World!
```

####  `POST /echo`

```bash
curl -X POST http://127.0.0.1:5000/echo -H "Content-Type: application/json" -d '{"message": "hello"}'
```

Returns:
```json
{
  "you_sent": {
    "message": "hello"
  }
}
```

####  `GET /pokemon/eevee`

```bash
curl http://127.0.0.1:5000/pokemon/eevee
```

Returns:
```json
{ "name": "eevee", ... }  // lots of data from the PokeAPI
```

---

###  8. (Optional) Add a `.gitignore` file

```bash
echo -e "venv/\n__pycache__/\n*.pyc\n.env" > .gitignore
```

🗒️ _This stops unnecessary stuff from getting committed to GitHub._

---

###  9. Create a `README.md` with instructions

Done — includes how to install dependencies, run the server, and test endpoints.

---

 What I Learned (Explained by a Dummy, for a Mentor)

- **What an HTTP server is**  
  It's just a program that waits for a request (like a knock at a door) and gives back a response (like an answer or gift).

- **What Flask does**  
  Makes building an HTTP server in Python easy — gives me tools to define routes (`/echo`, `/pokemon/<name>`, etc.)

- **What GET vs POST is**  
  - `GET` asks the server for info (like “what’s the weather?”)
  - `POST` sends info to the server (like “here’s my name, remember me”)

- **What JSON is**  
  It’s a format for sending data between programs. Looks like a Python dictionary with double quotes.

- **What the PokeAPI is**  
  A free online API that gives you data about Pokémon — my `/pokemon/<name>` route is just a wrapper around it.

- **How to use curl**  
  It’s like Postman, but in the terminal. It lets you test your API endpoints manually.

- **How to structure a project**  
  - Use `venv` to isolate dependencies (virtual environment)
  - Use `requirements.txt` to track them  
  - Use `README.md` to explain everything

---

 Final Thoughts

This project taught me how HTTP works at a deeper level, how APIs communicate, and how I can simulate a full backend app using nothing but Python, Flask, and a few commands. I now understand the client-server model much better — and know how to build and test my own RESTful API.

Side Note: To finally conclude this as a one man show, this was really made by a dummy. I know many would say "No that's not true". Believe me, it was made by a dummy, one who aspires and dreams =).
