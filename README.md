# Flask PokeAPI Proxy Server

This is a simple Flask HTTP server with the following features:

- `GET /` — returns "Hello World!"
- `POST /echo` — accepts JSON data and echoes it back
- `GET /pokemon/<name>` — proxies requests to the PokeAPI and returns Pokémon data

---

## Setup and Run Instructions

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME

Create and activate a Python Virtual Environment: This isolates your Python dependencies

python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

Instal Dependencies:
pip install -r requirements.txt

Run the server: This server will start locally at HTTP://127.0.0.1:5000
python app.py

Testing Endpoints: You can test endpoints using curl or any other API client

- GET / : curl HTTP://127.0.0.1:5000/

- POST /echo : curl -X POST http://127.0.0.1:5000/echo -H "Content-Type: application/json" -d '{"message":"hello"}'

- GET /pokemon/<name> : curl HTTP://127.0.0.1:5000/pokemon/base

Ensure you have internet access for the /pokemon/<name> endpoint, as it will fetch live data from the PokeAPI. The project will use Python 3.6+ and depends on Flash and Requests.

Explanation of Endpoints and HTTP Methods

Why these endpoints?
This Flask server demonstrates how to handle common HTTP request types and interact with external APIs, which is fundamental in web development.

1. POST /echo
Purpose:
This endpoint accepts JSON data sent by the client in the body of a POST request and responds by sending the same data back. It’s a simple way to test that the server can correctly receive and parse client data.

Why POST?
POST requests are designed to send data to the server. Unlike GET requests (which are for retrieving data), POST includes a body, allowing clients to submit structured data like JSON. This endpoint shows how to handle incoming data payloads.

2. GET /pokemon/<name>
Purpose:
This endpoint acts as a proxy to the external PokeAPI. When a client requests information about a Pokémon (by name), the server forwards the request to the PokeAPI, fetches the data, and returns it. This illustrates how a backend service can integrate external APIs and serve combined or filtered data.

Why GET?
GET requests are used to retrieve data from a server or API. Since this endpoint’s job is to fetch information (not change any data), GET is the appropriate HTTP method. The <name> in the URL path allows dynamic queries for different Pokémon.

3. GET /
Purpose:
A basic endpoint that returns a simple message ("Hello World!") to confirm the server is running and reachable.

Why GET?
GET is the standard method to fetch data or status without side effects. It’s commonly used for health checks or simple information retrieval.

Summary
POST /echo tests receiving and handling client-sent data.
GET /pokemon/<name> demonstrates fetching data from an external API and proxying it.
GET / verifies server availability.
Together, these endpoints provide a foundational example of handling common HTTP requests in a Python Flask app.
