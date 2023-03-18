import sqlite3
con = sqlite3.connect("tutorial.db")

cur = con.cursor()

cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 5526, 8.2),
        ('And Now for Something Completely Different', 69666, 7.5)
""")


con.commit()


res = cur.execute("SELECT score FROM movie")

res.fetchall()