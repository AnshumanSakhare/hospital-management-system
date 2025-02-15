create database hospital_db;
use hospital_db;
CREATE USER 'root'@'localhost' IDENTIFIED BY 'Pawara@123';
GRANT ALL PRIVILEGES ON hospital_db.* TO 'root'@'localhost';
FLUSH PRIVILEGES;
show tables;



use hospital_db;
desc tables;
show tables;
select*from auth_group;