-- 1번 
select profno 교수번호, name 교수이름, id ID
from professor
where left(id, 1) between 'A' and 'G';
-- -- 정규표현식 사용
select profno 교수번호, name 교수이름, id ID
from professor
where id regexp '^[A-G]'; 

-- 2번 
select profno 교수번호, name 교수이름, deptno 학과번호
from professor
where deptno in(101, 102);

-- 3번
select profno 교수번호,name 교수이름, hpage 홈페이지주소 
from professor
where hpage is not null; 

-- 4번 
select profno 교수번호, name 교수이름, deptno 학과번호, bonus BONUS
from professor
where bonus is not null;

-- 5번 
select studno 번호, name 이름, deptno1 학과번호
from student
union
select profno 번호, name 이름, deptno 학과번호
from professor
order by 학과번호 asc, 번호 desc;
