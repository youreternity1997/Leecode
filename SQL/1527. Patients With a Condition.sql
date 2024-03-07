#Approach 1
SELECT * FROM patients WHERE conditions REGEXP '\\bDIAB1'

#Approach 2
SELECT *
FROM Patients
WHERE conditions LIKE '% DIAB1%' OR conditions LIKE 'DIAB1%'