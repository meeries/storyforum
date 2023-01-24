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
