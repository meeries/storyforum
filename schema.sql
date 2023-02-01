DROP TABLE IF EXISTS users, categories, stories, comments, likes;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    category_name TEXT
);

CREATE TABLE stories (
    id SERIAL PRIMARY KEY,
    title TEXT,
    content TEXT,
    visible BOOLEAN,
    category_id INTEGER REFERENCES categories,
    user_id INTEGER REFERENCES users,
    created_at TIMESTAMP
);

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    content TEXT,
    user_id INTEGER REFERENCES users,
    story_id INTEGER REFERENCES stories,
    sent_at TIMESTAMP
);

CREATE TABLE likes (
    acc_id INTEGER REFERENCES users ON DELETE CASCADE,
    comm_id INTEGER REFERENCES comments ON DELETE CASCADE,
    PRIMARY KEY (acc_id, comm_id)
);

CREATE INDEX ON likes (comm_id)
;

INSERT INTO categories (category_name) VALUES
('Life'),
('Travel'),
('History'),
('Love'),
('Health'),
('Other');