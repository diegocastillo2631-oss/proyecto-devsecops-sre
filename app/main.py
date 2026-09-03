from flask import Flask, jsonify
import os
import pymysql

app = Flask(__name__)


def get_db_connection():
    return pymysql.connect(
        host=os.getenv("DB_HOST", "db"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "ejemplo"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME", "ejemplo"),
        cursorclass=pymysql.cursors.DictCursor,
    )


@app.route("/")
def home():
    return jsonify({
        "message": "API DevSecOps funcionando",
        "status": "ok"
    })


@app.route("/health")
def health():
    connection = None

    try:
        connection = get_db_connection()

        return jsonify({
            "database": "connected",
            "message": "API DevSecOps funcionando",
            "status": "ok"
        })

    except Exception as error:
        return jsonify({
            "database": "disconnected",
            "message": str(error),
            "status": "error"
        }), 500

    finally:
        if connection:
            connection.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # nosec B104
