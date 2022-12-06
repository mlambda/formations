from sqlalchemy import insert, text

# Style textuel
with engine.begin() as conn:
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 6, "y": 8}, {"x": 9, "y": 10}],
    )

# Utilisation des méthodes de SQLAlchemy Core
with engine.begin() as conn:
    conn.execute(insert(some_table), [{"x": 6, "y": 8}, {"x": 9, "y": 10}])
