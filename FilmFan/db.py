import sqlite3

def show_all_tables():
    conn = sqlite3.connect("data.sqlite")
    c = conn.cursor()

    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in c.fetchall()]

    conn.close()
    return tables