SELECT
    COUNT(DISTINCT lot_id) AS total_lots,
    COUNT(*) AS total_process_records,
    ROUND(AVG(yield_rate) * 100, 2) AS avg_yield_percent,
    ROUND(AVG(queue_time_hours + process_time_hours), 2) AS avg_cycle_time_hours,
    ROUND(SUM(process_time_hours), 2) AS total_process_hours,
    SUM(defect_count) AS total_defects
FROM fab_data;