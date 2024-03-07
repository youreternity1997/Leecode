#Approach 1
SELECT name 
FROM Customer 
WHERE referee_id !=2 
OR referee_id IS NULL;

#Approach 2
SELECT name
FROM Customer
WHERE id NOT IN (SELECT id FROM Customer WHERE referee_id = 2);

#Approach 3
SELECT name
FROM Customer
WHERE CASE 
        WHEN referee_id != 2 THEN 1
        WHEN referee_id IS NULL THEN 1
        ELSE 0
      END = 1;
