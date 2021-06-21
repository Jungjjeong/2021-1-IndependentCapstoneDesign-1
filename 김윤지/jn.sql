CREATE DATABASE factcheck default CHARACTER SET UTF8;

use factcheck;

CREATE TABLE User
(
	rate int,
    subject varchar(255),
    relation varchar(255),
    object varchar(255)
);

LOAD DATA LOCAL INFILE 'C:\\a.csv'
 