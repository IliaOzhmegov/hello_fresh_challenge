-- The system doesn't allow to create more than one account for one email
-- one possible solution can have a few nested subqueries

select product_sku
from product
where 
id_product in (select fk_product_subscribed_to
              from subscription
              where status = 'active' and fk_customer = (select id_customer from customer where email = 'fancygirl83@hotmail.com'));
