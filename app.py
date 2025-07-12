from flask import Flask, request, render_template_string, redirect
import pandas as pd

app = Flask(__name__)

watchlist = {}
unique_titles = set()

def get_watchlist_df():
    if not watchlist:
        return pd.DataFrame(columns=["Title", "Genres", "Rating"])
    return pd.DataFrame(watchlist.values())

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        title = request.form["title"]
        genres = request.form["genres"].split(",")
        try:
            rating = float(request.form["rating"])
        except ValueError:
            rating = -1
        
        if title in unique_titles:
            message = "❌ Movie already exists."
        elif not (0 <= rating <= 10):
            message = "❌ Rating must be between 0 and 10."
        else:
            watchlist[title] = {"Title": title, "Genres": genres, "Rating": rating}
            unique_titles.add(title)
            message = f"✅ Movie '{title}' added."

    df = get_watchlist_df()
    table_html = df.to_html(index=False) if not df.empty else "<p>🎞️ Watchlist is empty.</p>"

    html = """
    <h1>🎬 Movie Watchlist Manager</h1>
    <form method="post">
        <input type="text" name="title" placeholder="Movie Title" required><br><br>
        <input type="text" name="genres" placeholder="Genres (comma-separated)" required><br><br>
        <input type="number" step="0.1" name="rating" placeholder="Rating (0-10)" required><br><br>
        <button type="submit">Add Movie</button>
    </form>
    <p>{{ message }}</p>
    <h2>📋 Current Watchlist</h2>
    {{ table|safe }}
    <br><form method="post" action="/export"><button>Export to CSV</button></form>
    """
    return render_template_string(html, table=table_html, message=message)

@app.route("/export", methods=["POST"])
def export():
    df = get_watchlist_df()
    if not df.empty:
        df.to_csv("watchlist.csv", index=False)
        return "<p>✅ CSV file 'watchlist.csv' exported successfully.</p><br><a href='/'>Go back</a>"
    return "<p>⚠️ Watchlist is empty. Nothing to export.</p><br><a href='/'>Go back</a>"

if __name__ == "__main__":
    app.run(debug=True)
