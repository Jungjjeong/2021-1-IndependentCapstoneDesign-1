CREATE DATABASE factcheck default CHARACTER SET UTF8;

use factcheck;

CREATE TABLE sentence
(
	rate float,
    subject varchar(255),
    relation varchar(255),
    object varchar(255)
);
show tables;

LOAD DATA LOCAL INFILE "C:\\a.csv" INTO TABLE sentence
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
(rate, subject, relation, object);

SELECT * FROM factcheck.sentence;

SELECT JSON_OBJECT('rate',rate,'subject', subject, 'relation', relation, 'object', object) FROM sentence;
SELECT JSON_ARRAY(rate, subject, relation, object) FROM sentence;