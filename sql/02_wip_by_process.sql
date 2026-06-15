SELECT
    process_step,
    COUNT(*) AS wip_count
FROM fab_data
GROUP BY process_step
ORDER BY wip_count DESC;