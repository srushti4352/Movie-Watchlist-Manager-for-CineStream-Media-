# Movie-Watchlist-Manager-for-CineStream-Media-
# 🎬 Flask Movie Watchlist App

A simple Python Flask application to manage and display a movie watchlist. This is a beginner-friendly project built using Flask to learn the basics of backend development and routing.

---

## 🚀 Features

- Add movies with title, genre, and rating
- Display the complete movie watchlist
- Store data using CSV or in-memory (temporary)
- Run using local development server

---

## 🛠️ Tech Stack

- Python 3.10+
- Flask
- Pandas (if used for CSV handling)
- HTML/CSS (for frontend)

---

## 📂 Project Structure

Here’s a step-by-step Python project guide to build **Movie Watchlist Manager for CineStream Media** with code snippets that you can run in **Jupyter Notebook** or any Python IDE:

---

## ✅ **Step 1: Setup**

Make sure you have **Pandas** installed:

```bash
pip install pandas
```

---

## ✅ **Step 2: Import Libraries**

```python
import pandas as pd
```

---

## ✅ **Step 3: Initialize Data Structures**

```python
# Dictionary to store movie details
watchlist = {}

# Set to store unique titles
unique_titles = set()
```

---

## ✅ **Step 4: Add Movie Function**

```python
def add_movie(title, genres, rating):
    if title in unique_titles:
        print("❌ Movie already exists in the watchlist.")
        return
    if not (0 <= rating <= 10):
        print("❌ Invalid rating! Please enter a rating between 0 and 10.")
        return
    
    # Add movie to dictionary
    watchlist[title] = {
        "Title": title,
        "Genres": genres,
        "Rating": rating
    }
    unique_titles.add(title)
    print(f"✅ Movie '{title}' added successfully.")
```

---

## ✅ **Step 5: Remove Movie Function**

```python
def remove_movie(title):
    if title in watchlist:
        del watchlist[title]
        unique_titles.remove(title)
        print(f"🗑️ Movie '{title}' removed.")
    else:
        print("❌ Movie not found in watchlist.")
```

---

## ✅ **Step 6: Convert Watchlist to DataFrame**

```python
def get_watchlist_df():
    if not watchlist:
        return pd.DataFrame(columns=["Title", "Genres", "Rating"])
    
    return pd.DataFrame(watchlist.values())
```

---

## ✅ **Step 7: Filter by Genre**

```python
def filter_by_genre(genre):
    df = get_watchlist_df()
    filtered = df[df["Genres"].apply(lambda genres: genre.lower() in [g.lower() for g in genres])]
    return filtered
```

---

## ✅ **Step 8: Export Watchlist to CSV**

```python
def export_watchlist_to_csv(filename="watchlist.csv"):
    df = get_watchlist_df()
    df.to_csv(filename, index=False)
    print(f"📁 Watchlist exported to '{filename}'.")
```

---

## ✅ **Step 9: Display Watchlist**

```python
def show_watchlist():
    df = get_watchlist_df()
    if df.empty:
        print("🎞️ Watchlist is empty.")
    else:
        print("🎬 Current Watchlist:")
        display(df)  # Only works in Jupyter
```

> If **`display()`** gives an error in your environment, replace it with `print(df)`.

---

## ✅ **Step 10: Sample Usage**

```python
add_movie("Inception", ["Sci-Fi", "Action"], 9)
add_movie("Titanic", ["Romance", "Drama"], 8.5)
add_movie("Joker", ["Drama", "Thriller"], 8.8)

# Show all
show_watchlist()

# Filter by genre
print("🎭 Filtered by Drama:")
print(filter_by_genre("Drama"))

# Export to CSV
export_watchlist_to_csv()

# Remove a movie
remove_movie("Titanic")

Here's a **complete `README.md` file** for your Flask-based project (`app.py`). This is tailored for a beginner-friendly Flask app — you can modify it later for a larger project like **Fake Account Detection**.

---

## 📄 `README.md`

```markdown
# 🎬 Flask Movie Watchlist App

A simple Python Flask application to manage and display a movie watchlist. This is a beginner-friendly project built using Flask to learn the basics of backend development and routing.

---

## 🚀 Features

- Add movies with title, genre, and rating
- Display the complete movie watchlist
- Store data using CSV or in-memory (temporary)
- Run using local development server

---

## 🛠️ Tech Stack

- Python 3.10+
- Flask
- Pandas (if used for CSV handling)
- HTML/CSS (for frontend)

---

## 📂 Project Structure

```

project-folder/
│
├── app.py              # Main Flask application
├── templates/          # HTML templates
│   └── index.html      # Main UI
├── static/             # (Optional) CSS, JS files
│   └── style.css
├── watchlist.csv       # CSV file to store movie data
└── README.md           # Project documentation

````

---

## 🧪 Installation & Run Locally
````

### ✅ 2. Install dependencies

```bash
pip install flask pandas
```

> If you're not using Pandas/CSV, skip installing it.

### ✅ 3. Run the app

```bash
python app.py
```

### ✅ 4. Open in browser

Visit: `http://127.0.0.1:5000`


# output

![WhatsApp Image 2025-07-12 at 22 06 40_73064b5e](https://github.com/user-attachments/assets/b796bbbc-3272-4a23-888d-74596de7c837)




