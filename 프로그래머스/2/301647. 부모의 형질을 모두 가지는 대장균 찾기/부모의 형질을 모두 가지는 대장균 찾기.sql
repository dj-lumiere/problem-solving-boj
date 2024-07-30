-- 코드를 작성해주세요
select f.ID, f.GENOTYPE, g.GENOTYPE as PARENT_GENOTYPE
from ECOLI_DATA as f
join ECOLI_DATA as g
on f.PARENT_ID = g.ID
where f.GENOTYPE & g.GENOTYPE = g.GENOTYPE
order by f.id