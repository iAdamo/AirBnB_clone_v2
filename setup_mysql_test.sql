-- a script that prepares a MySQL server for the project
-- use 'Show Databse' to show database
-- use "SHOW GRANTS FOR 'hbnb_dev'@'localhost';"

CREATE DATABASE IF NOT EXIST hbnb_test_db;
CREATE USER IF NOT EXIST hbnb_test@localhost IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL ON hbnb_test_db.* TO hbnb_dev@localhost;
GRANT SELECT ON performance_schema.* TO hbnb_test@localhost;
