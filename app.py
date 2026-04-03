from flask import Flask, render_template
import mysql.connector
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Get password from environment variable
    db_password = os.getenv("DB_PASSWORD")

    # Connect to MySQL
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password=db_password,
        database="student_db"
    )

    cursor = db.cursor()

    # Fetch data
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template("index.html", students=data)

if __name__ == '__main__':
    app.run(debug=True)