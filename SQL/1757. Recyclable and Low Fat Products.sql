#Approach 1
select product_id from Products
where low_fats='Y' AND recyclable='Y'

#Approach 2
SELECT product_id
FROM (
    SELECT *
    FROM Products
    WHERE low_fats = 'Y'
) low_fat_products
WHERE low_fat_products.recyclable = 'Y';