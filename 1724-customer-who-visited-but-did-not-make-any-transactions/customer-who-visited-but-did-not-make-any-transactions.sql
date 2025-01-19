# Write your MySQL query statement below
select customer_id, count(*) as count_no_trans
from(
    select v.visit_id, t.visit_id as visit_t, customer_id, transaction_id
    From Visits as v
    left join Transactions as t
    on v.visit_id = t.visit_id
)
AS subquery
WHERE subquery.transaction_id IS NULL group by customer_id