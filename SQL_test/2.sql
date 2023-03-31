-- Not said what fields specificly we need to get, so let's get everything
-- That might need additional CTE.


-- option 1
select *
from customer
where id_customer in 
(select fk_customer
  from subscription
  where 
  status = 'active' and 
  fk_product_subscribed_to in (select id_product
                               from product
                               where fk_product_family in (select id_product_family from product_family where product_family_handle = 'classic-box')))


-- option 2: trying to make it more readable
WITH classic_box_products AS
(
  select id_product
  from product
  where fk_product_family in (select id_product_family from product_family where product_family_handle = 'classic-box')
),
customers_subscripted_to_classic_box AS
(
  select fk_customer
  from subscription
  where status = 'active' and fk_product_subscribed_to in (select * from classic_box_products)
)

select *
from customer
where id_customer in (select * from customers_subscripted_to_classic_box);
