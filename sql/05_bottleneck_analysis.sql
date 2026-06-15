WITH step_metrics AS (
    SELECT
        process_step,
        COUNT(*) AS wip_count,
        ROUND(AVG(queue_time_hours), 2) AS avg_queue_time_hours,
        ROUND(AVG(process_time_hours), 2) AS avg_process_time_hours,
        ROUND(AVG(queue_time_hours + process_time_hours), 2) AS avg_cycle_time_hours,
        ROUND(SUM(process_time_hours), 2) AS total_process_hours
    FROM fab_data
    GROUP BY process_step
)

SELECT
    process_step,
    wip_count,
    avg_queue_time_hours,
    avg_process_time_hours,
    avg_cycle_time_hours,
    total_process_hours,
    RANK() OVER (
        ORDER BY avg_queue_time_hours DESC
    ) AS queue_time_rank,
    RANK() OVER (
        ORDER BY avg_cycle_time_hours DESC
    ) AS cycle_time_rank,
    RANK() OVER (
        ORDER BY total_process_hours DESC
    ) AS workload_rank
FROM step_metrics
ORDER BY queue_time_rank;