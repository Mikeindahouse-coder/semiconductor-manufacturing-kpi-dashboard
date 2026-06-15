SELECT
    process_step,
    COUNT(*) AS record_count,
    ROUND(AVG(queue_time_hours), 2) AS avg_queue_time_hours,
    ROUND(AVG(process_time_hours), 2) AS avg_process_time_hours,
    ROUND(AVG(queue_time_hours + process_time_hours), 2) AS avg_cycle_time_hours,
    ROUND(
        AVG(queue_time_hours) * 100.0 /
        AVG(queue_time_hours + process_time_hours),
        2
    ) AS queue_time_percentage
FROM fab_data
GROUP BY process_step
ORDER BY avg_cycle_time_hours DESC;