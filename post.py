from flask import Flask, request, jsonify

app = Flask(__name__)

@app.post("/hello")
def hello():
    data = request.get_json()
    name = data.get("name")

    return jsonify({
        "message": f"Hello {name}!"
    })

if __name__ == "__main__":
    app.run(debug=True)