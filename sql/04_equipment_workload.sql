SELECT
    equipment_id,
    process_step,
    COUNT(*) AS lot_count,
    ROUND(SUM(process_time_hours), 2) AS total_process_hours,
    ROUND(AVG(process_time_hours), 2) AS avg_process_hours
FROM fab_data
GROUP BY equipment_id, process_step
ORDER BY total_process_hours DESC;