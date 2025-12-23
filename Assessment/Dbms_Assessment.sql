--SQL Query to Join Customer and Salesman Tables

 Create Customer table:

CREATE TABLE Customer (
    customer_id INT,
    cust_name VARCHAR(50),
    city VARCHAR(50),
    grade INT,
    salesman_id INT
);

--Insert data into Customer table

INSERT INTO Customer VALUES (3002, 'Nick Rimando', 'New York', 100, 5001);
INSERT INTO Customer VALUES (3007, 'Brad Davis', 'New York', 200, 5001);
INSERT INTO Customer VALUES (3005, 'Graham Zusi', 'California', 200, 5002);
INSERT INTO Customer VALUES (3008, 'Julian Green', 'London', 300, 5002);
INSERT INTO Customer VALUES (3004, 'Fabian Johnson', 'Paris', 300, 5006);
INSERT INTO Customer VALUES (3009, 'Geoff Cameron', 'Berlin', 100, 5003);
INSERT INTO Customer VALUES (3003, 'Jozy Altidor', 'Moscow', 200, 5007);
INSERT INTO Customer VALUES (3001, 'Brad Guzan', 'London', NULL, 5005);


Create Salesman table:

CREATE TABLE Salesman (
    salesman_id INT,
    name VARCHAR(50),
    city VARCHAR(50),
    commission DECIMAL(4, 2)
);

--Insert data into Salesman table:

INSERT INTO Salesman VALUES (5001, 'James Hoog', 'New York', 0.15);
INSERT INTO Salesman VALUES (5002, 'Nail Knite', 'Paris', 0.13);
INSERT INTO Salesman VALUES (5005, 'Pit Alex', 'London', 0.11);
INSERT INTO Salesman VALUES (5006, 'Mc Lyon', 'Paris', 0.14);
INSERT INTO Salesman VALUES (5007, 'Paul Adam', 'Rome', 0.13);
INSERT INTO Salesman VALUES (5003, 'Lauson Hen', 'San Jose', 0.12);

--Final JOIN query to get required result

SELECT 
    c.cust_name AS Customer_Name,
    c.city AS Customer_City,
    s.name AS Salesman_Name,
    s.commission AS Commission
FROM 
    Customer c
JOIN 
    Salesman s
ON 
    c.salesman_id = s.salesman_id;
