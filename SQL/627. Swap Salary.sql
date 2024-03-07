#Approach 1
update salary
set sex=if(sex='m','f','m');

#Approach 2
UPDATE Salary 
SET sex = (CASE WHEN sex = 'f' THEN 'm' ELSE 'f' END) 