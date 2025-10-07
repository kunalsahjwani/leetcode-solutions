CREATE FUNCTION getNthHighestSalary(N IN NUMBER) RETURN NUMBER IS
result NUMBER;
BEGIN
    select distinct salary into result from
    (select salary, dense_rank() over (order by salary desc) r
    from employee) where r = n;

    RETURN result;
END;