-- https://www.codewars.com/kata/576400f2f716ca816d001614/train/sql

CREATE OR REPLACE FUNCTION gdc1(numerator INT, denominator INT)
RETURNS int
language plpgsql
AS 
$$
DECLARE 
  zmienna INT = 1;
BEGIN
  WHILE MOD(denominator, numerator) != 0 LOOP
    zmienna = MOD(denominator, numerator);
    denominator = numerator;
    numerator = zmienna;
    END LOOP;
  RETURN zmienna;
END;
$$;

SELECT  numerator, 
        denominator, 
        numerator / gdc1(numerator, denominator) AS reduced_numerator, 
        denominator / gdc1(numerator, denominator) AS reduced_denominator
FROM fraction
ORDER BY numerator, denominator;