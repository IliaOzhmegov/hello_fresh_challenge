-- not sure what is meant here, how many times one particular product was ordered
-- or how divirse subscriptions for one particular client regarding products?
-- well, let's focus on the 2nd one


select
  count(*) as number_of_customers_that_ordered_more_than_one_product
from
(select fk_customer
 from subscription
 group by fk_customer having count(distinct fk_product_subscribed_to) > 1) as t
