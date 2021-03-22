DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS record_labels;

CREATE TABLE record_labels (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    location VARCHAR(255)
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    artist VARCHAR(255),
    format VARCHAR(255),
    genre VARCHAR(255),
    quantity INT,
    buy_cost FLOAT,
    sell_price FLOAT,
    record_label_id INT REFERENCES record_labels(id)
);