/*
  Time complexity: O(nlogn)
  Space complexity: O(k)
*/

select 
    sell_date, 
    count(distinct(product)) as num_sold, 
    GROUP_CONCAT(distinct(product) SEPARATOR  ',') as products 
from Activities
group by sell_date 
order by sell_date ASC;