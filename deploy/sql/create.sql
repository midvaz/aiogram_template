
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    telegram_id BIGINT NOT NULL,
    first_name  VARCHAR(255) DEFAULT NULL,
    last_name VARCHAR(255) DEFAULT NULL,
    user_name VARCHAR(255) DEFAULT NULL,
    phone_number varchar(20) DEFAULT NULL,
    create_at TIMESTAMP WITH TIME ZONE  DEFAULT now(),
    update_at TIMESTAMP WITH TIME ZONE  NULL,
    delete_at TIMESTAMP WITH TIME ZONE  NULL
);
