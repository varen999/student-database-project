from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    # Connect to MySQL
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="varensql",   # 👈 replace with your password
        database="student_db"
    )

    cursor = db.cursor()

    # Fetch data
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    # Close connection
    cursor.close()
    db.close()

    return render_template("index.html", students=data)

if __name__ == '__main__':
    app.run(debug=True)