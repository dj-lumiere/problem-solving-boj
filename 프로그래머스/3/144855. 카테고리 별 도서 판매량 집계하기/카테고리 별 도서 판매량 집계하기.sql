SELECT g.category, sum(f.sales)
from book_sales as f
join book as g
on f.book_id = g.book_id
where year(f.sales_date) = 2022 and month(f.sales_date) = 1
group by g.category
order by g.category