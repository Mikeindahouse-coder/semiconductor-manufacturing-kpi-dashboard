SELECT
    status,
    COUNT(*) AS record_count,
    ROUND(
        COUNT(*) * 100.0 / (SELECT COUNT(*) FROM fab_data),
        2
    ) AS percentage
FROM fab_data
GROUP BY status
ORDER BY record_count DESC;