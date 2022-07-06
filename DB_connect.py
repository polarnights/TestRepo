from sqlite3 import OperationalError

import psycopg2


def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connected successfully!")
    except OperationalError as e:
        print(f"Exception: '{e}'")
    return connection


connection = create_connection("postgres", "nickoliger", "", "127.0.0.1", "5432")


def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully!")
    except OperationalError as e:
        print(f"Exception: '{e}'")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


create_user_info = """
CREATE TABLE IF NOT EXISTS user_info
(
    first_name         VARCHAR,
    last_name          VARCHAR,
    middle_name        VARCHAR,
    user_id            INTEGER UNIQUE,
    phone_number       VARCHAR,
    age                INTEGER,
    citizenship        INTEGER,
    current_stage      VARCHAR,
    track              INTEGER,
    utc_update_time    INTEGER
);

COMMENT ON TABLE user_info IS '- Таблица с информацией о пользователе';

COMMENT ON COLUMN user_info.first_name IS '- Имя пользователя';

COMMENT ON COLUMN user_info.last_name IS '- Фамилия пользователя';

COMMENT ON COLUMN user_info.middle_name IS '- Отчество пользователя';

COMMENT ON COLUMN user_info.user_id IS '- Уникальный id пользователя';

COMMENT ON COLUMN user_info.phone_number IS '-  Номер телефона пользователя';

COMMENT ON COLUMN user_info.age IS '-  Возраст пользователя';

COMMENT ON COLUMN user_info.citizenship IS '-  Гражданство пользователя';

COMMENT ON COLUMN user_info.track IS '-  Текущий сценарий пользователя';

COMMENT ON COLUMN user_info.current_stage IS '-  Статус прохождения сценария';

COMMENT ON COLUMN user_info.utc_update_time IS '-  Последнее время редактирования';
"""

execute_query(connection, create_user_info)

users_TEST = [
    ("Vasily", "Petrov", "Sergeevich", "79091234567", 1),
    ("Anton", "Romanov", "Alexandrovich", "79993827117", 2),
    ("Semyon", "Skvortsov", "Nikolayevich", "79631228923", 3),
]

user_records_TEST = ", ".join(["%s"] * len(users_TEST))

insert_query = f"INSERT INTO user_info (first_name, last_name, middle_name, phone_number, track) VALUES {user_records_TEST}"

# connection.autocommit = True
# cursor = connection.cursor()
# cursor.execute(insert_query, users_TEST)


select_tracks = """
SELECT
  last_name,
  first_name,
  middle_name,
  phone_number,
  current_stage
FROM
  user_info
"""

tracks = execute_read_query(connection, select_tracks)

for track in tracks:
    if track[2] == 1:
        pass
    elif track[2] == 2:
        pass
    elif track[2] == 3:
        pass

# ---Testing section---
TESTER_COUNT = 1
print("Iteration #", TESTER_COUNT)
tracks = execute_read_query(connection, select_tracks)
for track in tracks:
    print(track)
print("-----------------------------")
# ---------------------
