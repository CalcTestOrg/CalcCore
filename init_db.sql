CREATE DATABASE CalculatorDB;

USE CalculatorDB;

CREATE TABLE [Results] (
    [ID] INT PRIMARY KEY IDENTITY,
    [Expression] VARCHAR(255),
    [Result] FLOAT,
    [timestamp] DATETIME DEFAULT GETDATE()
);

DROP TABLE [Results]
SELECT * FROM [Results];