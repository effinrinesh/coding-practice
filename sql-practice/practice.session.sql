CREATE TABLE employee (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(20),
    employee_division VARCHAR(20)
);

DESCRIBE employee;

DROP TABLE employee;


ALTER TABLE employee ADD employee_branch VARCHAR(20);

SELECT * FROM employee;

INSERT INTO employee VALUES (1, "SampleName","SampleDiv","SampleBranch")