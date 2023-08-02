use my_testdb;

-- 1번
select cust_name 고객이름, cust_jumin 주민등록번호, concat(left(cust_jumin, 6), '*******') "*표시"
from cust;

-- 2번
select name 교수이름, email email, substring_index(email, '@', -1) 도메인주소
from professor
where deptno = 101;

-- 3번
select empno 사원번호, name 사원이름, birthday 생일 
from emp
where year(birthday) = 1976;

-- 4번 
select deptno 학과번호, name 교수이름, pay 급여, format(pay*12, 0) 연봉
from professor
where deptno in(101, 102);

-- 5번 
select deptno1 학과번호, studno 학번, name 이름, birthday 생일 
from student
where month(birthday) in(10, 11, 12) and deptno1 in(101, 201);

-- 6번 
select mno 회원번호, mname 이름, ifnull(mgrade, '기본등급') 회원등급
from member2;

-- 7번
select gname 고객이름, point 보유포인트,
	case 
		when point > 900000 then 'VIP'
        when point > 600000 then 'GOLD'
        when point > 300000 then 'MIDDLE'
        else 'START'
	end 등급
from customer;

-- 8번 
select name, email, instr(email, '@') "INSTR()로 @ 위치"
from professor;

select name, email, locate('@', email) "LOCATE()로 @ 위치"
from professor;

-- 9번
select ename, job, sal
from emp3
where length(ename) > 5;

-- 10번 
select name, id, deptno
from professor
where length(id) < 6;

-- 11번 
select name, id, left(id, 4) "id에서 4글자"
from professor
where length(id) > 6 ; 

-- 12번
select name, email, substring_index(substring_index(email, '@', -1), '.', 1) "추출된 글자"
from professor
where deptno = 101;

-- 13번 
select name, id, tel, substring_index(substring_index(tel, ')', -1), '-', 1) "추출된 숫자"
from student
where length(id) > 6;

-- 14번
select name, id, concat(left(id, 4), repeat('*', (length(id) - 4))) "*로 숨기기"
from student
where deptno1 = 101;

-- 15번
select name, id, concat(left(id, 2), repeat('*', (length(id) - 2))) "*로 숨기기"
from professor
where deptno = 101;

-- 16번
select name, id, concat(repeat('*', length(id)-2), right(id, 2)) "*로 숨기기"
from professor
where deptno = 101;

-- 17번
select name, id, concat(left(id, 2), repeat('*', 2), right(id, length(id)-4)) "*로 바꾸기"
from professor;