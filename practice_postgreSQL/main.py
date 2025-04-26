import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# .env file load kar rahe hain
load_dotenv()

# DATABASE_URL ko environment se read kar rahe hain
DATABASE_URL = os.getenv("DATABASE_URL_UNPOOLED")

# SQLAlchemy engine create kar rahe hain
engine = create_engine(DATABASE_URL)


def main():
    with engine.connect() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            );
        """))
        conn.commit()
        conn.execute(text("""
             INSERT INTO users (name, email)
             VALUES ('Saif', 'saif@example.com'),
                    ('Haseeb', 'haseeb@example.com'),
                    ('Ammar', 'ammar@example.com');
         """))
        conn.commit()


        result = conn.execute(text("SELECT * FROM users;")).mappings()

        print("Users in database:")
        for row in result:
            print(dict(row)) 

if __name__ == "__main__":
    main()