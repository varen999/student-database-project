CREATE DATABASE student_db;

USE student_db;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    course VARCHAR(50)
);

INSERT INTO students (name, age, course) VALUES
('Aarav', 20, 'CSE'),
('Vihaan', 21, 'ECE'),
('Ishaan', 22, 'MECH'),
('Reyansh', 21, 'CSE'),
('Kabir', 22, 'ECE'),
('Arjun', 21, 'AERO'),
('Rohan', 20, 'MECH'),
('Dev', 22, 'CSE'),
('Kunal', 23, 'CIVIL');