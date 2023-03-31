-- solution with a simple nested query

select
 AVG(count) as avg_number_of_subscriptions
from
 (select count(*) as count from subscription group by fk_customer) as t
