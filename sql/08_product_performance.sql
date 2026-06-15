SELECT
    product_id,
    COUNT(DISTINCT lot_id) AS total_lots,
    ROUND(AVG(yield_rate) * 100, 2) AS avg_yield_percent,
    SUM(defect_count) AS total_defects,
    ROUND(AVG(defect_count), 2) AS avg_defects_per_step
FROM fab_data
GROUP BY product_id
ORDER BY avg_yield_percent DESC;