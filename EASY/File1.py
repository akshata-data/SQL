select product_id from products where low_fats  like "Y" and recyclable  like "Y";
select name from customer where referee_id not like 2 or referee_id is null;
select name, population, area from world where population >=25000000 or area >= 3000000;
select distinct author_id as id from views where author_id = viewer_id order by id;
select tweet_id from tweets where length(content)>15;

select id from (select *, lag(temperature) over (order by id) as lag_prev from weather) abc where temperature> lag_prev;

/*select customer_id, count(customer_id) count_no_trans from(select a.customer_id, b.transaction_id from visits a left join transactions b on a.visit_id = b.visit_id) abc
where transaction_id is nullgroup by customer_id;*/
select a.customer_id, count(a.customer_id) count_no_trans from visits a left join transactions b on a.visit_id=b.visit_id where b.transaction_id is null group by 1;
