-- 코드를 입력하세요
SELECT f.MCDP_CD as '진료과코드', count(f.APNT_YMD) as '5월예약건수'
from APPOINTMENT as f
where year(f.APNT_YMD)=2022 and month(f.APNT_YMD)=5
group by f.MCDP_CD
order by 5월예약건수, 진료과코드