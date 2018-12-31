DROP DATABASE IF EXISTS demo;

CREATE DATABASE demo;

USE demo
CREATE TABLE stocks(
    exchange  CHAR(6),
    symbol VARCHAR(7),
    company VARCHAR(50),
    volume  DECIMAL(20,1),
    price DECIMAL(10,2),
    changee DECIMAL(5,2),
    idsym VARCHAR(20),

    PRIMARY KEY (idsym)
);

