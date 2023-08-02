use my_testdb;
select name, hobby from emp;

select name, hobby,
			LPAD(hobby, 15, '*') "LAPD",
            RPAD(hobby, 15, '*') "RPAD"
from emp
where deptno in(1001, 1002, 1003);

select '02)123-4567' as "tel", instr('02)123-4567', ')') "INSTR";

select avg(pay) AVG, sum(pay) SUM, max(pay) MAX, min(pay) MIN
from professor
where deptno = 101;

select name, bonus from professor
where deptno = 101;

-- 데이터 건수를 출력하는 함수 count
select count(*) "* 사용", count(bonus) "bonus "
from professor
where deptno = 101;

-- 주어진 숫자보다 큰/ 작은 정수값 출력
-- -- dual은 사용자가 함수(계산)을 할 때 임시로 사용하는 테이블
select ceil(3.4) "CEIL_!", floor(3.4) "FLOOR_1"
from dual;
select 10 div 3 as "DIV_1", (10/3) "DIV_2", mod(10,3) "MOD"
from dual;
select round(10/3, 1) "ROUND_1", round(10/3,2) "Round_2",
	truncate(10/3, 1) "Truncate_1", truncate(10/3, 2) "truncate_2"
from dual;

-- 날짜 계산 함수
-- -- 현재 날짜/시간
select current_date(), current_time(), current_timestamp()
from dual;

-- -- 날짜 차이
select datediff(20231023, 20231001) "차이 일 수",
		period_diff(202112, 202101) "차이_개월 수"
from dual;

-- -- 날짜 더하기
select date_add('2022-01-10', interval 10 day) "10 next",
	date_add('2022-01-10', interval -10 day) "10 before"
from dual;

select date_add('2022-01-10 09:30:21', interval 15 minute) "15 minute next",
	date_add('2022-01-10 09:30:21', interval -15 minute) "15 minute before"
from dual; 

-- 월/주/연도
select dayname("2021-02-10 09:30:21") "DAYNAME",
	dayofmonth("2021-02-10 09:30:21") "DAY of MONTH",
    dayofweek("2021-02-10 09:30:21") "DAY of WEEK",
    dayofyear("2021-02-10 09:30:21") "DAY of YEAR"
from dual;

-- -- 달의 마지막 날 조회
select last_day("2021-02-10") "LASTDAY",
		makedate(2022, 40) "MAKEDATE",
        maketime("2021-02-10") "MAKETIME"
from dual;

select week("2022-02-10") "주", weekday("2022-02-10") "요일",
		month('2022-02-10') "월", year("2022-02-10") "년도"
from dual;

-- -- 날짜 형태 지정
select date_format(now(), '%Y-%m-%d %H:%i') "날짜 형태 지정하기"
from dual;

-- 숫자 천단위 구분 기호
select name, pay, format(pay, 0), format(pay,2)
from emp
where deptno in(1001,1002);

-- null값 다른 값으로 변환
select name, pay, bonus, 
	ifnull(bonus, 0) "ifnull", coalesce(bonus, 0) "coalesce", concat(format((pay*12) + bonus, 0), '원') "연봉"
from professor
where deptno in(101,102);

-- 데이터 유형 지정해 변환
select convert(100, char) "CON_CHAR", convert("10:30:45", time) "CON_TIME",
		cast("2022-01-10"as date) "CAST_DATE", cast("2022-01-10"as char) "CAST_CHAR"
from dual;