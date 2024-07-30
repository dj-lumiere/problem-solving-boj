-- 코드를 입력하세요
SELECT distinct c.CART_ID
FROM CART_PRODUCTS AS c
where 'Milk' in (
    select d.NAME
    from CART_PRODUCTS as d
    where d.CART_ID = c.CART_ID
) and 'Yogurt' in (
    select d.NAME
    from CART_PRODUCTS as d
    where d.CART_ID = c.CART_ID
)