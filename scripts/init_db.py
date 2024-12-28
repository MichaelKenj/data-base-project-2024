import psycopg2

DATABASE = "MichaelKenDB"
USER = "michaelKen"
PASSWORD = "michael2004"
HOST = "83.149.198.142"
PORT = 5419

def init_db():
    try:
        conn = psycopg2.connect(
            dbname="postgres", user=USER, password=PASSWORD, host=HOST, port=PORT
        )
        conn.autocommit = True
        cursor = conn.cursor()

        # Создаем базу данных
        cursor.execute(f"CREATE DATABASE {DATABASE} OWNER {USER};")
        print(f"База данных {DATABASE} успешно создана!")

    except psycopg2.Error as e:
        print(f"Ошибка при создании базы данных: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    init_db()
