from sqlalchemy import create_engine, text

# MySQL Connection Details
USER = 'root'               # Username
PASSWORD = 'rabia12345'       # Password
HOST = 'localhost'          # Local Server
DB_NAME = 'school'          # Target Database

engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DB_NAME}")

with engine.connect() as conn:

    conn.execute(text(
        """
        CREATE TABLE IF NOT EXISTS students (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(50) NOT NULL,
        age INT NOT NULL
            
        );
        """
    ))
# Insert a Sample Record
with engine.connect() as conn:
    conn.execute(text("""
        INSERT INTO students (name, age)
        VALUES ('rabia', 21),
               ('Ali', 20),
               ('Ahmed', 19);
    """))
    conn.commit()  # 🧠 Don't forget to commit the transaction