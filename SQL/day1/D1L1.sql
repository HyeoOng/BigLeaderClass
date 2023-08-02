use my_testdb;
select * from emp;
desc emp;
select name, birthday from emp;
select name, '안녕' from emp;
select concat(name, ' 안녕!') as "이름" from emp;

-- select empno as "사원번호", name "이름", birthday "생일" from emp;
select empno as 사원번호, name 이름, birthday 생일 from emp; -- 같은 결과 

select distinct name 이름 from emp; -- 중복제거

select name 이름, pay 급여, pay*2 as "급여 2배" from emp; -- 별칭은 실제 데이터를 수정한 것이 아님!

select
name 이름, pay 급여, pay*2 as 희망급여
from emp order by 급여 desc;   -- desc는 내림차순

select 
name as 사원명, pay 연봉, pay*2 희망급여
from emp
where pay >= 40000000 and pay <= 50000000
order by pay;

select 
name as 사원명, pay 연봉, pay*2 희망급여
from emp
where pay between 40000000 and 90000000
order by pay;

select 
name as 사원명, pay 연봉, pay*2 희망급여
from emp
where name like 'W%'
order by pay;
