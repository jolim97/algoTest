SELECT INS.ANIMAL_ID, INS.ANIMAL_TYPE, INS.NAME
FROM ANIMAL_INS INS
JOIN ANIMAL_OUTS OUTS
on INS.ANIMAL_ID = OUTS.ANIMAL_ID
where INS.SEX_UPON_INTAKE not in ('Spayed Female', 'Neutered Male') and OUTS.SEX_UPON_OUTCOME in ('Spayed Female', 'Neutered Male')
ORDER BY ANIMAL_ID;
