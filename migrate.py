from database import engine
from sqlalchemy import text

def migrate():
    with engine.connect() as connection:
        print("Checking/Adding columns to 'users' table...")
        try:
            connection.execute(text("ALTER TABLE users ADD COLUMN IF NOT EXISTS name VARCHAR;"))
            connection.execute(text("ALTER TABLE users ADD COLUMN IF NOT EXISTS password VARCHAR;"))
            connection.commit()
            print("Migration successful.")
        except Exception as e:
            print(f"Migration failed: {e}")

if __name__ == "__main__":
    migrate()
