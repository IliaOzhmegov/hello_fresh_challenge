-- So far I have been using nested subquery, why not use here inner join
-- also it's not stated what columns are desired so let's get only id_subscription

select 
  id_subscription
from
  (select 
    fk_subscription
    from `order`
    group by fk_subscription having count(fk_subscription) = 1) as o 
  inner join
  (select * from subscription where status = 'paused') as s on o.fk_subscription = s.id_subscription
