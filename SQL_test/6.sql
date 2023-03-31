-- wait, isn't a subscription for a particular client associated 
-- with only one product???
-- Like I might have been subscribed for several products but 
-- each product requires its own subscription
-- it does contradict with ER diagram, which I had to additionally request due to poor quality

-- solution from 5.sql
select
  count(*) as number_of_customers_that_ordered_more_than_one_product
from
(select fk_customer
 from subscription
 group by fk_customer having count(distinct fk_product_subscribed_to) > 1) as t
