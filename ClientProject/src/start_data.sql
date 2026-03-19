
-- ============================================================
--  No-Churn Telecom | Churn Count Query
--  Schema : project_telecom
--  Table  : telecom_churn_data
-- ============================================================
SELECT
    COUNT(*)                                    AS total_customers,
    SUM(CASE WHEN churn = 0 THEN 1 ELSE 0 END) AS no_churn,
    SUM(CASE WHEN churn = 1 THEN 1 ELSE 0 END) AS churned,
    ROUND(AVG(churn) * 100, 2)                 AS churn_rate_pct
FROM
    project_telecom.telecom_churn_data
    WHERE customer_id BETWEEN 1 AND 1000;