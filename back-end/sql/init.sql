#USUARIO MYSQL
CREATE USER 'caidaSiu'@'localhost'
IDENTIFIED BY '1234';

GRANT ALL PRIVILEGES
ON restaurant_db.*
TO 'caidaSiu'@'localhost';
FLUSH PRIVILEGES;