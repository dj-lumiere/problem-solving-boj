-- 코드를 입력하세요
SELECT f.PRODUCT_ID, g.PRODUCT_NAME, sum(g.PRICE*f.AMOUNT) as TOTAL_SALES
from FOOD_ORDER as f
join FOOD_PRODUCT as g
on f.PRODUCT_ID = g.PRODUCT_ID
where year(f.PRODUCE_DATE) = 2022 and month(f.PRODUCE_DATE) = 5
group by g.PRODUCT_ID
order by TOTAL_SALES desc, f.PRODUCT_ID