--a script that prepares a MySQL server for the project
--use 'Show Databse' to show database
--- use "SHOW GRANTS FOR 'hbnb_dev'@'localhost';"
CREATE DATABASE IF NOT EXIST hbnb_dev_db;
CREATE USER IF NOT EXIST 'hbnb_dev_db'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd'
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
