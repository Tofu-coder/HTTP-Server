✅ Flask HTTP Server Assignment - README.md

This project is a simple Flask web server that demonstrates the use of common HTTP methods (GET, POST) and API interaction. It includes a health check endpoint, a JSON echo endpoint, and an external API proxy for Pokémon data via the PokeAPI.

📌 Project Summary

Language: Python 3.6+
Framework: Flask
Purpose: Demonstrate understanding of HTTP methods, API endpoints, and external API calls.
Key Concepts: RESTful routing, JSON handling, third-party APIs, environment setup

🔧 Installation Instructions

1. Clone the Repository
Replace with your actual GitHub username and repo name:
```bash
git clone https://github.com/Tofu-Coder/HTTP-Server.git
cd HTTP-Server
```
2. Create and Activate a Python Virtual Environment
This isolates project dependencies:

```bash
python3 -m venv venv
source venv/bin/activate       # macOS/Linux

```
3. Fix and Install Dependencies
Ensure your requirements.txt contains:


Then install them:

```bash
pip install -r requirements.txt
```

4. Run the Server

```bash
python app.py
```
The flash app will start on:

```bash
http://127.0.0.1:5000
```

🔁 API Endpoints

✅ GET /
Description: Basic health check to confirm server is running.

Example:

```bash
curl http://127.0.0.1:5000/
```
Response:

```bash
Hello World! 
```
✅ POST /echo
Description: Accepts JSON input and echoes it back, wrapped in a dictionary.

Example:

```bash
curl -X POST http://127.0.0.1:5000/echo \
     -H "Content-Type: application/json" \
     -d '{"message":"hello"}'
```

Response:

```bash
{
  "you_sent": {
    "message": "hello"
  }
}
```
✅ GET /pokemon/<name>
Description: Fetches live Pokémon data from PokeAPI. Returns 404 if Pokémon not found.

Example:

```bash
curl http://127.0.0.1:5000/pokemon/eevee
```
Response: Full JSON object representing the Pokémon.

Error Example:

```bash
curl http://127.0.0.1:5000/pokemon/unknown
```
Response:

```bash
{
  "error": "Pokémon not found"
}
```
🔗 Internet access is required for this endpoint to function.

📝 Code Explanation

```bash
GET /
```
Returns "Hello World!" — a simple GET endpoint.

Common in health checks or minimal RESTful apps.

```bash
POST /echo
```
Accepts Content-Type: application/json and echoes back the data.

Demonstrates how to handle client-sent JSON with a POST request.

```bash
GET /pokemon/<name>
```
Shows how to fetch external data from an API (PokeAPI).
Uses the Pokémon name as a dynamic route parameter.
Demonstrates how to handle external HTTP requests in Flask (requests.get()).

📦 File Structure

```bash
YOUR_REPO_NAME/
├── app.py               # Main Flask app
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```
✅ Dependencies (Fixed)

```bash
Flask==2.3.3
requests==2.31.0
```
Make sure these are the only two entries in requirements.txt.
