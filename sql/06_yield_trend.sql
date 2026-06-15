SELECT
    DATE(end_time) AS production_date,
    ROUND(AVG(yield_rate) * 100, 2) AS avg_yield_percent
FROM fab_data
WHERE yield_rate IS NOT NULL
GROUP BY DATE(end_time)
ORDER BY production_date;