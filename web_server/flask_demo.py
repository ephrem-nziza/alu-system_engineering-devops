from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/add", methods=["GET"])
def add():
    try:
        num1 = request.args.get("num1", type=int)
        num2 = request.args.get("num2", type=int)

        if num1 is None or num2 is None:
            return jsonify({"error": "Both 'num1' and 'num2' are required"}), 400

        if not isinstance(num1, int) or not isinstance(num2, int):
            return jsonify({"error": "Both 'num1' and 'num2' must be integers"}), 400

        result = num1 + num2
        return jsonify({"result": result}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":

    app.run(debug=True, host = "0.0.0.0", port = 5000)
