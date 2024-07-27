CREATE DATABASE simpledb;
USE simpledb;
CREATE TABLE messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    message VARCHAR(255) NOT NULL
);
INSERT INTO messages (message) VALUES ('Hello from the database!');
