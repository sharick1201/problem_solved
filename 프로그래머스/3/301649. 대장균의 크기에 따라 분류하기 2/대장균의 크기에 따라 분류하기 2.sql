WITH ECOLI_DATA_CTE AS (
    
    SELECT
        ID,
        NTILE(4) OVER (ORDER BY SIZE_OF_COLONY DESC) AS sizeRank
    FROM
        ECOLI_DATA
)
SELECT
    ID,
    CASE
        WHEN sizeRank = 1 THEN 'CRITICAL'
        WHEN sizeRank = 2 THEN 'HIGH'
        WHEN sizeRank = 3 THEN 'MEDIUM'
        WHEN sizeRank = 4 THEN 'LOW'
    END AS COLONY_NAME
FROM
    ECOLI_DATA_CTE
ORDER BY
    ID;