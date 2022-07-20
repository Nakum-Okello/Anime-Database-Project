import csv


from cs50 import SQL 

open ("Animes.db","w").close()


db = SQL("sqlite:///Animes.db")

db.execute("CREATE TABLE Anime(id INTEGER PRIMARY KEY, title TEXT, episodes INTEGER, ranked INTEGER)")
db.execute("CREATE TABLE Genre(id INTEGER PRIMARY KEY, popularity INTEGER, score FLOAT)")

db.execute("CREATE TABLE Members (anime_id INTEGER, genre_id INTEGER, FOREIGN KEY(anime_id) REFERENCES Anime(id), FOREIGN KEY(genre_id) REFERENCES Genre(id))")


with open("Animes.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:
        title_name= row["title"]
        episode=row["episodes"]
        rank=row["ranked"]
        fame=row["popularity"]
        scores=row["score"]

        Anime =db.execute("INSERT INTO Anime( title, episodes, ranked) VALUES(?,?,?)",title_name,episode,rank)
        Genre= db.execute("INSERT INTO Genre(popularity, score) VALUES(?,?)",fame,scores)

        Members= db.execute("INSERT INTO Members(anime_id,genre_id) VALUES((SELECT id FROM Anime WHERE id =?),(SELECT id FROM Genre WHERE id =?))",Anime,Genre)