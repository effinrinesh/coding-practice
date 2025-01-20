CREATE TABLE employee (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(20),
    employee_division VARCHAR(20)
);

DESCRIBE employee;

DROP TABLE employee;


ALTER TABLE employee ADD employee_branch VARCHAR(20);

SELECT * FROM employee;

INSERT INTO employee VALUES (2, "Abc","Data Science","London")

INSERT INTO employee (employee_id, employee_division, employee_branch) VALUES (3,"Business Analytics", "Manchester")