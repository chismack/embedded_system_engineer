CREATE DATABASE iot;
USE iot;

CREATE TABLE sensor_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    voltage FLOAT,
    current FLOAT,
    power FLOAT,
    temperature FLOAT,
    cooler_status BOOLEAN,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
