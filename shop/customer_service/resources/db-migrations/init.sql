DROP TABLE IF EXISTS customer;
DROP TABLE IF EXISTS customer_order;
DROP TABLE IF EXISTS customer_favorite_items;
DROP TABLE IF EXISTS users;

CREATE TABLE customer (
    id INT(11) NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(45) NULL,
    last_name VARCHAR(45) NULL,
    email VARCHAR(45) NULL,
    status ENUM('REGULAR','VIP','IN_ACTIVE') NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE customer_order (
    id INT(11) NOT NULL AUTO_INCREMENT,
    customer_id INT(11) NOT NULL,
    item_name VARCHAR(400) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (customer_id) REFERENCES customer(id)
);

CREATE TABLE customer_favorite_items (
    id INT(11) NOT NULL AUTO_INCREMENT,
    customer_id INT(11) NOT NULL,
    item_id INT(11) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (customer_id) REFERENCES customer(id)
);

CREATE TABLE users (
    id INT(11) NOT NULL AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    PRIMARY KEY(id)
);
