

SELECT 
    Churn,
    COUNT(*) as кількість,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM `telco-customer-churn`), 1) as відсоток
FROM `telco-customer-churn`
GROUP BY Churn;

SELECT 
    Contract,
    COUNT(*) as кількість,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) as пішло,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1) as churn_rate
FROM `telco-customer-churn`
GROUP BY Contract
ORDER BY churn_rate DESC;

SELECT 
    PaymentMethod,
    COUNT(*) as кількість,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1) as churn_rate
FROM `telco-customer-churn`
GROUP BY PaymentMethod
ORDER BY churn_rate DESC;

SELECT 
    CASE 
        WHEN tenure <= 12 THEN '0-12 місяців'
        WHEN tenure <= 24 THEN '13-24 місяці'
        WHEN tenure <= 48 THEN '25-48 місяців'
        ELSE '49+ місяців'
    END as сегмент,
    COUNT(*) as кількість,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1) as churn_rate
FROM `telco-customer-churn`
GROUP BY сегмент
ORDER BY churn_rate DESC;