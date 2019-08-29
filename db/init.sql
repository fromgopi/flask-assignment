CREATE DATABASE IF  NOT EXISTS `flask_demo_wekan`;

CREATE USER 'wekan'@'%' IDENTIFIED BY 'wekan';

USE `flask_demo_wekan`;

GRANT ALL ON flask_demo_wekan.* TO 'wekan'@'%' WITH GRANT OPTION;

CREATE TABLE `test`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(55) NOT NULL
);
