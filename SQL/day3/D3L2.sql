alter table big_leader.student
add constraint fk_student_table
foreign key (소속)
references big_leader.class(소속);


-- view 시작
-- -- 단순뷰
select * from emp3;
create view vemp
as 
	select empno, ename, deptno
	from emp3
    where deptno in(10, 20);

-- -- 복합뷰
create or replace view vemp3
as 
	select e.name, d.dname, e.deptno
    from emp3 e, dept3 d
    where e.deptno = d.deptno
    and e.detpno = 10;
    
select e.deptno, d.dname, e.max_sal
from (select deptno, MAX(sal) max_sal
		from emp3
        group by deptno) e, dept3 d
where d.deptno = e.deptno;

-- 253페이지 연습문제
select * from professor;
select * from department;

-- -- 1번
create or replace view prof_dept_view
as 
	select p.profno 교수번호, p.name 교수명, d.dname 소속학과명
    from professor p
    join department d
    on p.deptno = d.deptno;
select * from prof_dept_view;

-- -- 2번
select d.dname, s.max_height, s.max_weight
from (select deptno1, max(height) max_height, max(weight) max_weight
		from student
        group by deptno1) s, department d
where d.deptno = s.deptno1;

select * from riss_title.title;