from sqlalchemy import create_engine, text

DB_FILE = "myTest.db"

# Create an SQLite engine connected to the real database
engine = create_engine(f"sqlite:///{DB_FILE}")

# Open a connection to the database
with engine.connect() as conn:
     conn.execute(text(
        """
        CREATE TABLE IF NOT EXISTS person_table (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(25) NOT NULL,
            age INTEGER
        );
        """
    ))
with engine.connect() as conn:
    conn.execute(
        text("INSERT INTO person_table (name, age) VALUES (:name, :age)"),
        [
            {"name": "Samreen", "age": 25},
            {"name": "Amber", "age": 30},
            {"name": "Bob", "age": 35},
            {"name": "Alice", "age": 40},
            {"name": "Charlie", "age": 45},
        ]
    )
    conn.commit()

# with engine.connect() as conn:
    # conn.execute(text(
    #     """
    #     DELETE FROM person_table
    #     WHERE name =='Samreen';
    #     """
    # ))

    # conn.commit()

# with engine.connect() as conn:
     
#      conn.execute(
#         text(
#             """
#             UPDATE person_table
#             SET age = 50
#             WHERE name == 'Bob';
#             """
#         )
#      )
#      conn.commit()