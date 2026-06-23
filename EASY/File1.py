select id from (select *, lag(temperature) over (order by id) as lag_prev from weather) abc where temperature> lag_prev;
