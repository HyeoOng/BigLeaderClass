-- 테이블 생성
create table temp_1(
	no int,
    name char(10),
    birthday date);
    
desc temp_1;

-- Default 값 사용
create table temp_2(
	no int default 9999,
    name varchar(10) default 'aaa',
    tel varchar(15) default '111-222-3333');
    
desc temp_2;

-- 값 입력
insert into temp_2(no) value(1);
select * from temp_2;

-- 다른 테이블 복사
create table temp_3 like emp3;