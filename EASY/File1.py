select id from (select *, lag(temperature) over (order by id) as lag_prev from weather) abc where temperature> lag_prev;

/*select customer_id, count(customer_id) count_no_trans from(select a.customer_id, b.transaction_id from visits a left join transactions b on a.visit_id = b.visit_id) abc
where transaction_id is nullgroup by customer_id;*/
select a.customer_id, count(a.customer_id) count_no_trans from visits a left join transactions b on a.visit_id=b.visit_id where b.transaction_id is null group by 1;
