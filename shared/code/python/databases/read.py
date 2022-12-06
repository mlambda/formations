from sqlalchemy import select, text

# Style textuel
with engine.begin() as conn:
    result = conn.execute(text("SELECT x, y FROM some_table"))
    for row in result:
        print(f"x: {row.x}  y: {row.y}")

# Utilisation des méthodes de SQLAlchemy Core
with engine.begin() as conn:
    result = conn.execute(select(some_table.c.x, some_table.c.y))
