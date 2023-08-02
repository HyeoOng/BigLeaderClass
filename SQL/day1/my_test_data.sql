-- 알려드립니다 
-- 이 자료는 SQL 능력자 교재용 실습용 데이터입니다
-- 아래 데이터는 저자인 서진수의 저작물로 저작권 보호를 받습니다
-- 아래 데이터를 본 교재의 교육용이 아닌 다른 용도로 사용할 경우
-- 법적 조치를 받을 수 있으니 유의하시기 바랍니다.
-- 본 교재와 자료 사용 관련 문의는 seojinsu@gmail.com 으로 문의주세요

USE my_testdb ;

-- 연습용 테이블 생성 후 데이터 입력하기
DROP TABLE IF EXISTS  cust ;
CREATE TABLE cust (
cust_number  CHAR(8)  primary key , 
cust_name VARCHAR(20) NOT NULL , 
cust_jumin CHAR(13) NOT NULL , 
cust_point INT NULL )  ;

insert into cust values (20010001,'James Seo','7510231369824',980000);
insert into cust values (20010002,'Mel Gibson','7502241128467',73000);
insert into cust values (20010003,'Bruce Willis','7506152123648',320000);
insert into cust values (20010004,'Bill Pullman','7512251063421',65000);
insert into cust values (20010005,'Liam Neeson','7503031639826',180000);
insert into cust values (20010006,'Samuel Jackson','7601232186327',153000);
insert into cust values (20010007,'Ahnjihye','7604212298371',273000);
insert into cust values (20010008,'Jim Carrey','7609112118379',315000);
insert into cust values (20010009,'Morgan Freeman','7601202378641',542000);
insert into cust values (20010010,'Arnold Scharz','7610122196482',265000);
insert into cust values (20010011,'Brad Pitt','7711291186223',110000);
insert into cust values (20010012,'Michael Douglas','7704021358674',99000);
insert into cust values (20010013,'Robin Williams','7709131276431',470000);
insert into cust values (20010014,'Tom Hanks','7702261196365',298000);
insert into cust values (20010015,'Angela Bassett','7712141254963',420000);
insert into cust values (20010016,'Jessica Lange','7808192157498',598000);
insert into cust values (20010017,'Winona Ryder','7801051776346',625000);
insert into cust values (20010018,'Michelle Pfeiffer','7808091786954',670000);
insert into cust values (20010019,'Whoopi Goldberg','7803242114563',770000);
insert into cust values (20010020,'Emma Thompson','7802232116784',730000);
commit ;

DROP  TABLE IF EXISTS  gift ;
create table gift
( gno  int ,
  gname varchar(30) ,
  g_start  int ,
  g_end  int );

insert into gift values(1,'Tuna Set',1,100000);
insert into gift values(2,'Shampoo Set',100001,200000);
insert into gift values(3,'Car wash Set',200001,300000);
insert into gift values(4,'Kitchen Supplies Set',300001,400000);
insert into gift values(5,'Mountain bike',400001,500000);
insert into gift values(6,'LCD Monitor',500001,600000);
insert into gift values(7,'Notebook',600001,700000);
insert into gift values(8,'Wall-Mountable TV',700001,800000);
insert into gift values(9,'Drum Washing Machine',800001,900000);
insert into gift values(10,'Refrigerator',900001,1000000);
commit ;


DROP  TABLE IF EXISTS customer ;

create table customer
(gno  int ,
 gname char(30) ,
 jumin char(13) ,
 point int)  ;

insert into customer values (20010001,'James Seo','7510231369824',980000);
insert into customer values (20010002,'Mel Gibson','7502241128467',73000);
insert into customer values (20010003,'Bruce Willis','7506152123648',320000);
insert into customer values (20010004,'Bill Pullman','7512251063421',65000);
insert into customer values (20010005,'Liam Neeson','7503031639826',180000);
insert into customer values (20010006,'Samuel Jackson','7601232186327',153000);
insert into customer values (20010007,'Ahnjihye','7604212298371',273000);
insert into customer values (20010008,'Jim Carrey','7609112118379',315000);
insert into customer values (20010009,'Morgan Freeman','7601202378641',542000);
insert into customer values (20010010,'Arnold Scharz','7610122196482',265000);
insert into customer values (20010011,'Brad Pitt','7711291186223',110000);
insert into customer values (20010012,'Michael Douglas','7704021358674',99000);
insert into customer values (20010013,'Robin Williams','7709131276431',470000);
insert into customer values (20010014,'Tom Hanks','7702261196365',298000);
insert into customer values (20010015,'Angela Bassett','7712141254963',420000);
insert into customer values (20010016,'Jessica Lange','7808192157498',598000);
insert into customer values (20010017,'Winona Ryder','7801051776346',625000);
insert into customer values (20010018,'Michelle Pfeiffer','7808091786954',670000);
insert into customer values (20010019,'Whoopi Goldberg','7803242114563',770000);
insert into customer values (20010020,'Emma Thompson','7802232116784',730000);
commit ;

DROP  TABLE IF EXISTS  emp ;
CREATE TABLE EMP (
 EMPNO       INT  PRIMARY KEY,
 NAME        VARCHAR(30) NOT NULL,
 BIRTHDAY    DATE,
 DEPTNO      CHAR(6) NOT NULL,
 EMP_TYPE    VARCHAR(30),
 TEL         VARCHAR(15),
 HOBBY       VARCHAR(30),
 PAY         INT,
 POSITION    VARCHAR(30),
 PEMPNO      INT
);

INSERT INTO EMP VALUES (19900101,'Kurt Russell','1964-01-25','0001','Permanent employee','054)223-0001','music',100000000,'Boss',null);
INSERT INTO EMP VALUES (19960101,'AL Pacino','1973-03-22','1000','Permanent employee','02)6255-8000','reading',72000000,'Department head',19900101);
INSERT INTO EMP VALUES (19970201,'Woody Harrelson','1975-04-15','1000','Permanent employee','02)6255-8005','Fitness',50000000,'Section head',19960101);
INSERT INTO EMP VALUES (19930331,'Tommy Lee Jones','1976-05-25','1001','Perment employee','02)6255-8010','bike',60000000,'Deputy department head',19960101);
INSERT INTO EMP VALUES (19950303,'Gene Hackman','1973-06-15','1002','Perment employee','02)6255-8020','Marathon',56000000,'Section head',19960101);
INSERT INTO EMP VALUES (19966102,'Kevin Bacon','1972-07-05','1003','Perment employee','052)223-4000','Music',75000000,'Department head',19900101);
INSERT INTO EMP VALUES (19930402,'Hugh Grant','1972-08-15','1004','Perment employee','042)998-7005','Climb',51000000,'Section head',19966102);
INSERT INTO EMP VALUES (19960303,'Keanu Reeves','1971-09-25','1005','Perment employee','031)564-3340','Climb',35000000,'Deputy Section chief',19966102);
INSERT INTO EMP VALUES (19970112,'Val Kilmer','1976-11-05','1006','Perment employee','054)223-4500','Swim',68000000,'Department head',19900101);
INSERT INTO EMP VALUES (19960212,'Chris O''Donnell','1972-12-15','1007','Perment employee','054)223-4600',null,49000000,'Section head',19970112);
INSERT INTO EMP VALUES (20000101,'Jack Nicholson','1985-01-25','1008','Contracted Worker','051)123-4567','Climb', 30000000,'',19960212);
INSERT INTO EMP VALUES (20000102,'Denzel Washington','1983-03-22','1009','Contracted Worker','031)234-5678','Fishing', 30000000,'',19960212);
INSERT INTO EMP VALUES (20000203,'Richard Gere','1982-04-15','1010','Contracted Worker','02)2345-6789','Baduk', 30000000,'',19960212);
INSERT INTO EMP VALUES (20000334,'Kevin Costner','1981-05-25','1011','Contracted Worker','053)456-7890','Singing', 30000000,'',19960212);
INSERT INTO EMP VALUES (20000305,'JohnTravolta','1980-06-16','1008','Probation','051)567-8901','Reading book', 22000000,'',19960212);
INSERT INTO EMP VALUES (20006106,'Robert De Niro','1980-07-05','1009','Probation','031)678-9012','Driking',   22000000,'',19960212);
INSERT INTO EMP VALUES (20000407,'Sly Stallone','1980-08-15','1010','Probation','02)2789-0123','Computer game', 22000000,'',19960212);
INSERT INTO EMP VALUES (20000308,'Tom Cruise','1980-09-25','1011','Intern','053)890-1234','Golf', 20000000,'',19960212);
INSERT INTO EMP VALUES (20000119,'Harrison Ford','1980-11-05','1004','Intern','042)901-2345','Drinking',   20000000,'',19930402);
INSERT INTO EMP VALUES (20000210,'Clint Eastwood','1980-12-15','1005','Intern','031)345-3456','Reading book', 20000000,'',19960303);
COMMIT;

DROP  TABLE IF EXISTS  emp2 ;
CREATE TABLE EMP2 (
 EMPNO       INT  PRIMARY KEY,
 NAME        VARCHAR(30) NOT NULL,
 BIRTHDAY    DATE,
 DEPTNO      CHAR(6) NOT NULL,
 EMP_TYPE    VARCHAR(30),
 TEL         VARCHAR(15),
 HOBBY       VARCHAR(30),
 PAY         INT,
 BONUS       INT,
 POSITION    VARCHAR(30),
 PEMPNO      INT
);

INSERT INTO EMP2 VALUES (19900101,'Kurt Russell','1964-01-25','0001','Permanent employee','054)223-0001','music',100000000,null,'Boss',null);
INSERT INTO EMP2 VALUES (19960101,'AL Pacino','1973-03-22','1000','Permanent employee','02)6255-8000','reading',72000000,400,'Department head',19900101);
INSERT INTO EMP2 VALUES (19970201,'Woody Harrelson','1975-04-15','1000','Permanent employee','02)6255-8005','Fitness',50000000,200,'Section head',19960101);
INSERT INTO EMP2 VALUES (19930331,'Tommy Lee Jones','1976-05-25','1001','Perment employee','02)6255-8010','bike',60000000,250,'Deputy department head',19960101);
INSERT INTO EMP2 VALUES (19950303,'Gene Hackman','1973-06-15','1002','Perment employee','02)6255-8020','Marathon',56000000,0,'Section head',19960101);
INSERT INTO EMP2 VALUES (19966102,'Kevin Bacon','1972-07-05','1003','Perment employee','052)223-4000','Music',75000000,null,'Department head',19900101);
INSERT INTO EMP2 VALUES (19930402,'Hugh Grant','1972-08-15','1004','Perment employee','042)998-7005','Climb',51000000,null,'Section head',19966102);
INSERT INTO EMP2 VALUES (19960303,'Keanu Reeves','1971-09-25','1005','Perment employee','031)564-3340','Climb',35000000,450,'Deputy Section chief',19966102);
INSERT INTO EMP2 VALUES (19970112,'Val Kilmer','1976-11-05','1006','Perment employee','054)223-4500','Swim',68000000,null,'Department head',19900101);
INSERT INTO EMP2 VALUES (19960212,'Chris O''Donnell','1972-12-15','1007','Perment employee','054)223-4600',null,49000000,150,'Section head',19970112);
INSERT INTO EMP2 VALUES (20000101,'Jack Nicholson','1985-01-25','1008','Contracted Worker','051)123-4567','Climb', 30000000,230,'',19960212);
INSERT INTO EMP2 VALUES (20000102,'Denzel Washington','1983-03-22','1009','Contracted Worker','031)234-5678','Fishing', 30000000,null,'',19960212);
INSERT INTO EMP2 VALUES (20000203,'Richard Gere','1982-04-15','1010','Contracted Worker','02)2345-6789','Baduk',30000000,100,'',19960212);
INSERT INTO EMP2 VALUES (20000334,'Kevin Costner','1981-05-25','1011','Contracted Worker','053)456-7890','Singing', 30000000,120,'',19960212);
INSERT INTO EMP2 VALUES (20000305,'JohnTravolta','1980-06-16','1008','Probation','051)567-8901','Reading book', 22000000,null,'',19960212);
INSERT INTO EMP2 VALUES (20006106,'Robert De Niro','1980-07-05','1009','Probation','031)678-9012','Driking',   22000000,80,'',19960212);
INSERT INTO EMP2 VALUES (20000407,'Sly Stallone','1980-08-15','1010','Probation','02)2789-0123','Computer game', 22000000,null,'',19960212);
INSERT INTO EMP2 VALUES (20000308,'Tom Cruise','1980-09-25','1011','Intern','053)890-1234','Golf', 20000000,null,'',19960212);
INSERT INTO EMP2 VALUES (20000119,'Harrison Ford','1980-11-05','1004','Intern','042)901-2345','Drinking',   20000000,50,'',19930402);
INSERT INTO EMP2 VALUES (20000210,'Clint Eastwood','1980-12-15','1005','Intern','031)345-3456','Reading book', 20000000,null,'',19960303);
COMMIT;

DROP  TABLE IF EXISTS  emp3 ;
CREATE TABLE EMP3 ( 
  EMPNO     INT, 
  ENAME     CHAR(10), 
  JOB       CHAR(9), 
  MGR       INT, 
  HIREDATE  DATE, 
  SAL       INT,
  COMM      INT, 
  DEPTNO    INT) ;

insert into emp3 values (7369,'SMITH','CLERK',7902,'1980-12-17',800,null,20);
insert into emp3 values (7499,'ALLEN','SALESMAN',7698,'1981-02-20',1600,300,30);
insert into emp3 values (7521,'WARD','SALESMAN',7698,'1982-02-22',1250,500,30);
insert into emp3 values (7566,'JONES','MANAGER',7839,'1981-04-02',2975,null,20);
insert into emp3 values (7654,'MARTIN','SALESMAN',7698,'1981-09-28',1250,1400,30);
insert into emp3 values (7698,'BLAKE','MANAGER',7839,'1981-05-01',2850,null,30);
insert into emp3 values (7782,'CLARK','MANAGER',7839,'1981-06-09',2450,null,10);
insert into emp3 values (7839,'KING','PRESIDENT',null,'1981-11-17',5000,null,10);
insert into emp3 values (7844,'TURNER','SALESMAN',7698,'1981-09-08',1500,0,30);
insert into emp3 values (7900,'JAMES','CLERK',7698,'1981-12-03',950,null,30);
insert into emp3 values (7902,'FORD','ANALYST',7566,'1981-12-03',3000,null,20);
insert into emp3 values (7934,'MILLER','CLERK',7782,'1982-01-23',1300,null,10);

DROP  TABLE IF EXISTS  dept ;

CREATE TABLE DEPT (
 DCODE   VARCHAR(6)  PRIMARY KEY,
 DNAME   VARCHAR(30) NOT NULL,
 PDEPT VARCHAR(6) ,
 AREA        VARCHAR(30)
);

INSERT INTO DEPT VALUES ('0001','President','','Pohang Main Office');
INSERT INTO DEPT VALUES ('1000','Management Support Team','0001','Seoul Branch Office');
INSERT INTO DEPT VALUES ('1001','Financial Management Team','1000','Seoul Branch Office');
INSERT INTO DEPT VALUES ('1002','General affairs','1000','Seoul Branch Office');
INSERT INTO DEPT VALUES ('1003','Engineering division','0001','Pohang Main Office');
INSERT INTO DEPT VALUES ('1004','H/W Support Team','1003','Daejeon Branch Office');
INSERT INTO DEPT VALUES ('1005','S/W Support Team','1003','Kyunggi Branch Office');
INSERT INTO DEPT VALUES ('1006','Business Department','0001','Pohang Main Office');
INSERT INTO DEPT VALUES ('1007','Business Planning Team','1006','Pohang Main Office');
INSERT INTO DEPT VALUES ('1008','Sales1 Team','1007','Busan Branch Office');
INSERT INTO DEPT VALUES ('1009','Sales2 Team','1007','Kyunggi Branch Office');
INSERT INTO DEPT VALUES ('1010','Sales3 Team','1007','Seoul Branch Office');
INSERT INTO DEPT VALUES ('1011','Sales4 Team','1007','Ulsan Branch Office');

commit;

DROP  TABLE IF EXISTS hakjum ;
create table hakjum
(grade char(3) NOT NULL ,
 min_point  int ,
 max_point  int );

insert into hakjum values ('A+',96,100);
insert into hakjum values ('A0',90,95);
insert into hakjum values ('B+',86,89);
insert into hakjum values ('B0',80,85);
insert into hakjum values ('C+',76,79);
insert into hakjum values ('C0',70,75);
insert into hakjum values ('D',0,69);

DROP  TABLE IF EXISTS score ;
create table score
(studno  int ,
 score int);

insert into score values (9411,97);
insert into score values (9412,78);
insert into score values (9413,83);
insert into score values (9414,62);
insert into score values (9415,88);
insert into score values (9511,92);
insert into score values (9512,87);
insert into score values (9513,81);
insert into score values (9514,79);
insert into score values (9515,95);
insert into score values (9611,89);
insert into score values (9612,77);
insert into score values (9613,86);
insert into score values (9614,82);
insert into score values (9615,87);
insert into score values (9711,91);
insert into score values (9712,88);
insert into score values (9713,82);
insert into score values (9714,83);
insert into score values (9715,84);

DROP  TABLE IF EXISTS professor ;
create table professor
(profno int(4) primary key,
 name  varchar(20) not null, 
 id  varchar(15) not null,
 position varchar (30) not null,
 pay int (3) not null,
 hiredate  date not null,
 bonus int(4) ,
 deptno  int(3),
 email  varchar(50),
 hpage  varchar(50)) ;

insert into professor
values(1001,'Audie Murphy','Murphy','a full professor',550,'1980-06-23',100,101,'captain@abc.net','http://www.abc.net');

insert into professor
values(1002,'Angela Bassett','Bassett','assistant professor',380,'1987-01-30',60,101,'sweety@abc.net','http://www.abc.net');

insert into professor
values (1003,'Jessica Lange','Lange','instructor',270,'1998-03-22',null,101,'pman@power.com','http://www.power.com');

insert into professor
values (2001,'Winona Ryder','Ryder','instructor',250,'2001-09-01',null,102,'lamb1@hamail.net',null);

insert into professor
values (2002,'Michelle Pfeiffer','Pfeiffer','assistant professor',350,'1985-11-30',80,102,'number1@naver.com','http://num1.naver.com');

insert into professor
values (2003,'Whoopi Goldberg','Goldberg','a full professor',490,'1982-04-29',90,102,'bdragon@naver.com',null);

insert into professor
values (3001,'Emma Thompson','Thompson','a full professor',530,'1981-10-23',110,103,'angel1004@hanmir.com',null);

insert into professor
values (3002,'Julia Roberts','Roberts','assistant professor',330,'1997-07-01',50,103,'naone10@empal.com',null);

insert into professor
values (3003,'Sharon Stone','Stone','instructor',290,'2002-02-24',null,103,'only_u@abc.com',null);

insert into professor
values (4001,'Meryl Streep','Streep','a full professor',570,'1981-10-23',130,201,'chebin@daum.net',null);

insert into professor
values (4002,'Susan Sarandon','Sarandon','assistant professor',330,'2009-08-30',null,201,'gogogo@def.com',null);

insert into professor
values (4003,'Nicole Kidman','Kidman','assistant professor',310,'1999-12-01',50,202,'mypride@hanmail.net',null);

insert into professor
values (4004,'Holly Hunter','Hunter','instructor',260,'2009-01-28',null,202,'ironman@naver.com',null);

insert into professor
values (4005,'Meg Ryan','Ryan','a full professor',500,'1985-09-18',80,203,'standkang@naver.com',null);

insert into professor 
values (4006,'Andie Macdowell','Macdowell','instructor',220,'2010-06-28',null,301,'napeople@jass.com',null);

insert into professor
values (4007,'Jodie Foster','Foster','assistant professor',290,'2001-05-23',30,301,'silver-her@daum.net',null);

DROP  TABLE IF EXISTS department ;

create table department
( deptno int(3) primary key ,
  dname varchar(50) not null,
  part int(3),
  build  varchar(30)) ;

insert into department 
values (101,'Computer Engineering',100,'Information Bldg');

insert into department
values (102,'Multimedia Engineering',100,'Multimedia Bldg');

insert into department
values (103,'Software Engineering',100,'Software Bldg');

insert into department
values (201,'Electronic Engineering',200,'Electronic Control Bldg');

insert into department
values (202,'Mechanical Engineering',200,'Machining Experiment Bldg');

insert into department
values (203,'Chemical Engineering',200,'Chemical Experiment Bldg');

insert into department
values (301,'Library and Information science',300,'College of Liberal Arts');

insert into department
values (100,'Department of Computer Information',10,null);

insert into department
values (200,'Department of Mechatronics',10,null);

insert into department
values (300,'Department of Humanities and Society',20,null);

insert into department
values (10,'College of Engineering',null,null);

insert into department
values (20,'College of Liberal Arts',null,null);

commit;
 

DROP  TABLE IF EXISTS student ;

create table student
( studno int(4) primary key,
  name   varchar(30) not null,
  id varchar(20) not null unique,
  grade int check(grade >= 1 and grade  <=6),
  jumin char(13) not null,
  birthday  date,
  tel varchar(15),
  height  int(4),
  weight  int(3),
  deptno1 int(3),
  deptno2 int(3),
  profno  int(4)) ;

insert into student values (
9411,'James Seo','75true',4,'7510231901813','1975-10-23','055)381-2158',180,72,101,201,1001);

insert into student values (
9412,'Rene Russo','Russo',4,'7502241128467','1975-02-24','051)426-1700',172,64,102,null,2001);

insert into student values (
9413,'Sandra Bullock','Bullock',4,'7506152123648','1975-06-15','053)266-8947',168,52,103,203,3002);

insert into student values (
9414,'Demi Moore','Moore',4,'7512251063421','1975-12-25','02)6255-9875',177,83,201,null,4001);

insert into student values (
9415,'Danny Glover','Glover',4,'7503031639826','1975-03-03','031)740-6388',182,70,202,null,4003);

insert into student values (
9511,'Billy Crystal','Crystal',3,'7601232186327','1976-01-23','055)333-6328',164,48,101,null,1002);

insert into student values (
9512,'Nicholas Cage','Cage',3,'7604122298371','1976-04-12','051)418-9627',161,42,102,201,2002);

insert into student values (
9513,'Micheal Keaton','Keaton',3,'7609112118379','1976-09-11','051)724-9618',177,55,202,null,4003);

insert into student values (
9514,'Bill Murray','Murray',3,'7601202378641','1976-01-20','055)296-3784',160,58,301,101,4007);

insert into student values (
9515,'Macaulay Culkin','Culkin',3,'7610122196482','1976-10-12','02)312-9838',171,54,201,null,4001);

insert into student values (
9611,'Richard Dreyfus','Dreyfus',2,'7711291186223','1977-11-29','02)6788-4861',182,72,101,null,1002);

insert into student values (
9612,'Tim Robbins','Robbins',2,'7704021358674','1977-04-02','055)488-2998',171,70,102,null,2001);

insert into student values (
9613,'Wesley Snipes','Snipes',2,'7709131276431','1977-09-13','053)736-4981',175,82,201,null,4002);

insert into student values (
9614,'Steve Martin','Martin',2,'7702261196365','1977-02-26','02)6175-3945',166,51,201,null,4003);

insert into student values (
9615,'Daniel Day-Lewis','Day-Lewis',2,'7712141254963','1977-12-14','051)785-6984',184,62,301,null,4007);

insert into student values (
9711,'Danny Devito','Devito',1,'7808192157498','1978-08-19','055)278-3649',162,48,101,null,null);

insert into student values (
9712,'Sean Connery','Connery',1,'7801051776346','1978-01-05','02)381-5440',175,63,201,null,null);

insert into student values (
9713,'Christian Slater','Slater',1,'7808091786954','1978-08-09','031)345-5677',173,69,201,null,null);

insert into student values (
9714,'Charlie Sheen','Sheen',1,'7803241981987','1978-03-24','055)423-9870',179,81,102,null,null);

insert into student values (
9715,'Anthony Hopkins','Hopkins',1,'7802232116784','1978-02-23','02)6122-2345',163,51,103,null,null);

commit;

DROP  TABLE IF EXISTS cal ;

CREATE TABLE cal
   (weekno  char(1),
    day   char(5),
    dayno char(2)) ; 

insert into cal values ('1','SUN','1');
insert into cal values ('1','MON','2');
insert into cal values ('1','TUE','3');
insert into cal values ('1','WED','4');
insert into cal values ('1','THU','5');
insert into cal values ('1','FRI','6');
insert into cal values ('1','SAT','7');
insert into cal values ('2','SUN','8');
insert into cal values ('2','MON','9');
insert into cal values ('2','TUE','10');
insert into cal values ('2','WED','11');
insert into cal values ('2','THU','12');
insert into cal values ('2','FRI','13');
insert into cal values ('2','SAT','14');
insert into cal values ('3','SUN','15');
insert into cal values ('3','MON','16');
insert into cal values ('3','TUE','17');
insert into cal values ('3','WED','18');
insert into cal values ('3','THU','19');
insert into cal values ('3','FRI','20');
insert into cal values ('3','SAT','21');
insert into cal values ('4','SUN','22');
insert into cal values ('4','MON','23');
insert into cal values ('4','TUE','24');
insert into cal values ('4','WED','25');
insert into cal values ('4','THU','26');
insert into cal values ('4','FRI','27');
insert into cal values ('4','SAT','28');
insert into cal values ('5','SUN','29');
insert into cal values ('5','MON','30');
insert into cal values ('5','TUE','31');
commit ;

DROP  TABLE IF EXISTS panmae ;
create table panmae
( p_date char(8) ,
  p_code int,
  p_qty  int ,
  p_total int ,
  p_store char(5) ) ;

insert into panmae values ('20110101',100,3,2400,'1000');
insert into panmae values ('20110101',101,5,4500,'1001');
insert into panmae values ('20110101',102,2,2000,'1003');
insert into panmae values ('20110101',103,6,5400,'1004');
insert into panmae values ('20110102',102,2,2000,'1000');
insert into panmae values ('20110102',103,5,4500,'1002');
insert into panmae values ('20110102',104,3,2400,'1002');
insert into panmae values ('20110102',105,2,3000,'1000');
insert into panmae values ('20110103',100,10,8000,'1004');
insert into panmae values ('20110103',100,2,1600,'1000');
insert into panmae values ('20110103',100,3,2400,'1001');
insert into panmae values ('20110103',101,4,3600,'1003');
insert into panmae values ('20110104',100,2,1600,'1002');
insert into panmae values ('20110104',100,4,3200,'1003');
insert into panmae values ('20110104',100,5,4000,'1004');
insert into panmae values ('20110104',101,3,2700,'1001');
insert into panmae values ('20110104',101,4,3600,'1002');
insert into panmae values ('20110104',101,3,2700,'1003');
insert into panmae values ('20110104',102,4,4000,'1001');
insert into panmae values ('20110104',102,2,2000,'1002');
insert into panmae values ('20110104',103,2,1800,'1003');

commit;

DROP  TABLE IF EXISTS loan ;
create table loan
( l_date char(8),
  l_code int,
  l_qty  int ,
  l_total int ,
  l_store char(5) );


insert into loan values ('20110101',100,3,2400,'1000');
insert into loan values ('20110101',101,5,4500,'1001');
insert into loan values ('20110101',102,2,2000,'1003');
insert into loan values ('20110101',103,6,5400,'1004');
insert into loan values ('20110102',102,2,2000,'1000');
insert into loan values ('20110102',103,5,4500,'1002');
insert into loan values ('20110102',104,3,2400,'1002');
insert into loan values ('20110102',105,2,3000,'1000');
insert into loan values ('20110103',100,10,8000,'1004');
insert into loan values ('20110103',100,2,1600,'1000');
insert into loan values ('20110103',100,3,2400,'1001');
insert into loan values ('20110103',101,4,3600,'1003');
insert into loan values ('20110104',100,2,1600,'1002');
insert into loan values ('20110104',100,4,3200,'1003');
insert into loan values ('20110104',100,5,4000,'1004');
insert into loan values ('20110104',101,3,2700,'1001');
insert into loan values ('20110104',101,4,3600,'1002');
insert into loan values ('20110104',101,3,2700,'1003');
insert into loan values ('20110104',102,4,4000,'1001');
insert into loan values ('20110104',102,2,2000,'1002');
insert into loan values ('20110104',103,2,1800,'1003');

commit;

DROP  TABLE IF EXISTS dept3 ;

CREATE TABLE DEPT3 (
  DEPTNO   int, 
  DNAME    CHAR(14), 
  LOC        CHAR(13));

insert into dept3 values (10,'ACCOUNTING','NEW YORK');
insert into dept3 values (20,'RESEARCH','DALLAS');
insert into dept3 values (30,'SALES','CHICAGO');
insert into dept3 values (40,'OPERATIONS','BOSTON');


DROP  TABLE IF EXISTS  member ;
CREATE TABLE member
( mno  int primary key,
  mname varchar(30) ,
  mid  varchar(20),
  mtel  varchar(20),
  mgrade varchar(10) );

DROP  TABLE IF EXISTS  ordered ;
CREATE TABLE ordered (
ordno int primary key ,
mno int ,
pname varchar(30) , 
qty int, 
price int );

insert into member values (2022001,'James Seo','75true','055)381-2158','C');
insert into member values (2022002,'Rene Russo','Russo','051)426-1700','C');
insert into member values (2022003,'Sandra Bullock','Bullock','053)266-8947','C');
insert into member values (2022004,'Demi Moore','Moore','02)6255-9875','C');
insert into member values (2022005,'Danny Glover','Glover','031)740-6388','C');

insert into ordered values(2022100101,2022001,'apple',3,3000) ;
insert into ordered values(2022100102,2022001,'beer',1,2000) ;
insert into ordered values(2022100103,2022001,'orange',1,1000) ;
insert into ordered values(2022100104,2022001,'apple',3,3000) ;
insert into ordered values(2022100105,2022001,'peach',2,4000) ;
insert into ordered values(2022100106,2022002,'grape',3,5000) ;
insert into ordered values(2022100107,2022002,'tomato',3,5000) ;
insert into ordered values(2022100108,2022003,'cherry',1,2500) ;
insert into ordered values(2022100109,2022004,'peach',3,6000) ;
insert into ordered values(2022100110,2022005,'grape',3,5000) ;



DROP  TABLE IF EXISTS  member2 ;
CREATE TABLE member2
( mno  int primary key,
  mname varchar(30) ,
  mid  varchar(20),
  mtel  varchar(20),
  mgrade varchar(10) );

insert into member2 values (2022001,'James Seo','75true','055)381-2158',NULL);
insert into member2 values (2022002,'Rene Russo','Russo','051)426-1700',NULL);
insert into member2 values (2022003,'Sandra Bullock','Bullock','053)266-8947','C');
insert into member2 values (2022004,'Demi Moore','Moore','02)6255-9875',NULL);
insert into member2 values (2022005,'Danny Glover','Glover','031)740-6388','C');

DROP  TABLE IF EXISTS  customer3 ;
CREATE TABLE customer3
( cno  int primary key,
  cname varchar(30) ,
  cid  varchar(20),
  mtel  varchar(20),
  mgrade varchar(10) );

insert into customer3 values (2022001,'James Seo','75true','055)381-2158',NULL);
insert into customer3 values (2022002,'Rene Russo','Russo','051)426-1700',NULL);
insert into customer3 values (2022003,'Sandra Bullock','Bullock','053)266-8947','C');
insert into customer3 values (2022004,'Demi Moore','Moore','02)6255-9875',NULL);
insert into customer3 values (2022005,'Danny Glover','Glover','031)740-6388','C');

DROP  TABLE IF EXISTS  product3 ;
CREATE TABLE product3
( pno  int primary key,
  pname varchar(30) ,
  price int );

insert into product3 values (1001,'apple',2000);
insert into product3 values (1002,'banana',500);
insert into product3 values (1003,'cherry',2500);
insert into product3 values (1004,'water melon',18000);
insert into product3 values (1005,'peach',500);

DROP  TABLE IF EXISTS  sales3 ;
CREATE TABLE sales3
( sno  int primary key, /*판매번호*/
  pno int , /*  제품 번호 */
  cno int , /* 구매 고객 번호 */
  qty int /*구매수량*/ );

insert into sales3 values (100001,1001,2022001, 5);
insert into sales3 values (100002,1001,2022002, 3);
insert into sales3 values (100003,1002,2022001, 2);
insert into sales3 values (100004,1003,2022001, 2);
insert into sales3 values (100005,1001,2022003, 1);
insert into sales3 values (100006,1004,2022001, 2);

/* 트리�