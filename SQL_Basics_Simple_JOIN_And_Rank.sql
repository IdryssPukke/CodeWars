SELECT 
  people.id,
  people.name, 
  COUNT(sales.sale) as sale_count, 
  RANK() OVER (ORDER BY people.name) sale_rank
  
FROM people FULL JOIN sales ON people.id = sales.people_id
GROUP BY people.id;