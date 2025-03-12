CREATE DATABASE CalculatorDB;

USE CalculatorDB;

CREATE TABLE Results (
    id INT PRIMARY KEY IDENTITY(1,1),
    expression NVARCHAR(255),
    result FLOAT,
    timestamp DATETIME DEFAULT GETDATE()
);


SELECT * FROM Results;
