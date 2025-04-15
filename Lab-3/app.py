from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

notes = []  # In-memory notes list

# Home route
@app.route('/')
def home():
    return render_template_string("""
        <h1>📝 Simple Notes Manager</h1>
        <form action="/add" method="post">
            <input type="text" name="note" placeholder="Enter your note" required>
            <button type="submit">Add Note</button>
        </form>
        <h2>📋 All Notes:</h2>
        <ul>
        {% for note in notes %}
            <li>{{ note }}</li>
        {% endfor %}
        </ul>
    """, notes=notes)

# Add note route
@app.route('/add', methods=['POST'])
def add_note():
    note = request.form.get('note')
    if note:
        notes.append(note)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
