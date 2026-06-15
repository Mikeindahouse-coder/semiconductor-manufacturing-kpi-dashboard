SELECT
    DATE(end_time) AS production_date,
    COUNT(DISTINCT lot_id) AS throughput
FROM fab_data
GROUP BY DATE(end_time)
ORDER BY production_date;