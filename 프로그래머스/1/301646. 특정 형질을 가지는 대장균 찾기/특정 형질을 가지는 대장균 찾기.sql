SELECT count(*) as count
FROM ECOLI_DATA 
WHERE (GENOTYPE & 2 = 0) AND ((GENOTYPE & 1 != 0) OR (GENOTYPE & 4 != 0))