# Open a connection
connection = sqlite3.connect("sql/database.db")
cursor = connection.cursor()

# Create tables in a dataset
query = f"""CREATE TABLE movies 
        ({", ".join([
            "title TEXT",
            "director_id TEXT",
            "release_date TEXT",
            "type TEXT"])});"""
cursor.execute(query)
# Insert values
query = f"""INSERT INTO movies VALUES ({",".join(
        "?" for i in range(len(movies[0]))
        )})"""
for movie in movies:
    cursor.execute(query, movie)
# Commit the database modifications
connection.commit()
connection.close()
