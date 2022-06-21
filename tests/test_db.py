
import psycopg2


def test_db():
    conn = psycopg2.connect(dbname="demo", user="postgres", password="postgres")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books;")
    result = cur.fetchone()
    print(result)
