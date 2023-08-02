create table dept4(
	deptno int primary key ,
    dname varchar(10) not null,
    loc varchar(10) not null);

    
insert into dept4 values(10, '총무부', '3F');
insert into dept4 values(20, '생산부', '1F');
insert into dept4 values(30, '영업부', '2F');

select * from dept4;

    