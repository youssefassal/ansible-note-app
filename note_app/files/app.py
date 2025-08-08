from flask import Flask, request, render_template_string
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)
DB_PATH = '/home/ec2-user/note_app/notes.db'

# Ensure DB and table exist
def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS notes
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT, created_at TEXT)''')
    conn.commit()
    conn.close()

init_db()

HTML_TEMPLATE = """
<!doctype html>
<title>Note Taking App</title>
<h1>Write your note here...</h1>
<form method="POST">
    <textarea name="content" rows="4" cols="50"></textarea><br>
    <button type="submit">Save Note</button>
</form>
<hr>
{% for note in notes %}
    <p>🕒 {{note[2]}}</p>
    <p>📌 {{note[1]}}</p>
    <hr>
{% endfor %}
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        content = request.form.get("content")
        if content.strip():
            conn = sqlite3.connect(DB_PATH)
            c = conn.cursor()
            c.execute("INSERT INTO notes (content, created_at) VALUES (?, ?)",
                      (content.strip(), datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            conn.commit()
            conn.close()
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM notes ORDER BY created_at DESC")
    notes = c.fetchall()
    conn.close()
    return render_template_string(HTML_TEMPLATE, notes=notes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

