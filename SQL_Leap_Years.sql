select
  year,
  CAST(
    CASE
      WHEN (year % 4 = 0 AND year % 100 != 0) or (year % 400 = 0)
        THEN true
      ELSE false 
      END AS Boolean 
  ) AS is_leap
from years
order by year; 
