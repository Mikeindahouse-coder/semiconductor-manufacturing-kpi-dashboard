SELECT
    process_step,
    ROUND(AVG(queue_time_hours), 2) AS avg_queue_time_hours,
    ROUND(MAX(queue_time_hours), 2) AS max_queue_time_hours,
    ROUND(MIN(queue_time_hours), 2) AS min_queue_time_hours
FROM fab_data
GROUP BY process_step
ORDER BY avg_queue_time_hours DESC;