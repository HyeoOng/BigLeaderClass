-- Having 절의 이해
select deptno, count(deptno), sum(pay), max(pay), min(pay)
from professor
group by deptno
having count(deptno) >= 2;

select deptno, position, sum(pay), max(pay), min(pay)
from professor
where year(hiredate) > 1990
group by deptno, position;

-- JOIN
select e. deptno, e.ename '사원이름', d.dname '부서이름'
from emp3 e join dept3 d
on e.deptno = d.deptno;

-- select * from emp3; 
-- select * from dept3;

-- -- 2개 이상의 테이블 조인
select 학생.name '학생이름', 학과.dname '학과이름', 교수.name '지도교수명'
from  student 학생
join department 학과 on 학생.deptno1 = 학과.deptno
join professor 교수 on 학생.profno = 교수.profno;