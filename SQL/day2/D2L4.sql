-- 주요 DML 사용하기
create table temp_8(
	no int default 9999,
    name varchar(10) default 'aaa',
    birth datetime default current_timestamp);

# 데이터 입력하기
insert into temp_8(no, name, birth)
values(1, '홍길동', '1975-10-23');
insert into temp_8 values(2, '전우치', '1982-07-15');
insert into temp_8(no, name) values(3, '강감찬');

# 다른 테이블 데이터 복사해 입력하기
create table temp_9
as select * from emp3 where 1=2;

insert into temp_9
select * from emp3
where sal <= 1500; 

# 테이블 삭제 - 삭제 전 safe updates 체크 풀어야함
delete from temp_8
where no = 2;

select * from temp_8;


