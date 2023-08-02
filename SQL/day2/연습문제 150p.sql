-- 연습문제 150p
select * from emp3;
-- 1번
select deptno "부서번호", format(sum(pay), 0) as "부서별 급여합계"
from emp
where deptno between 1001 and 1004
group by deptno
-- having sum(pay) >= 60000000
order by deptno ;

-- 2번 
select deptno,
	sum(if(job = 'CLERK', sal, 0)) "CLERK",
    sum(if(job = 'MANAGER', sal, 0)) "MANAGER",
    sum(if(job = 'PRESIDENT', sal, 0)) "PRESIDENT",
    sum(if(job = 'ANALYST', sal, 0)) "ANALYST",
    sum(if(job = 'SALESMAN', sal, 0)) "SALESMAN",
	sum(sal) "TOTAL"
from emp3
group by deptno
with rollup;

-- 3번
