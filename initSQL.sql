CREATE TABLE IF NOT EXISTS user_info
(
    first_name         VARCHAR,
    last_name          VARCHAR,
    middle_name        VARCHAR,
    phone_number       INTEGER,
    age                INTEGER,
    citizenship        INTEGER,
    current_stage      INTEGER,
    track              INTEGER,
    utc_update_time    INTEGER
);

COMMENT ON TABLE user_info IS '- Таблица с информацией о пользователе';

COMMENT ON COLUMN user_info.first_name IS '- Имя пользователя';

COMMENT ON COLUMN user_info.last_name IS '- Фамилия пользователя';

COMMENT ON COLUMN user_info.middle_name IS '- Отчество пользователя';

COMMENT ON COLUMN user_info.phone_number IS '-  Номер телефона пользователя';

COMMENT ON COLUMN user_info.age IS '-  Возраст пользователя';

COMMENT ON COLUMN user_info.citizenship IS '-  Гражданство пользователя';

COMMENT ON COLUMN user_info.track IS '-  Текущий сценарий пользователя';

COMMENT ON COLUMN user_info.current_stage IS '-  Статус прохождения сценария';

COMMENT ON COLUMN user_info.utc_update_time IS '-  Последнее время редактирования';