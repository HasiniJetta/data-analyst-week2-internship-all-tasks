USE sales_analysis;

SELECT
    customer_name,
    SUM(total_price) AS total_spent
FROM sales_data
GROUP BY customer_name
ORDER BY total_spent DESC
LIMIT 10;

SELECT
    AVG(total_price) AS average_order_value
FROM sales_data;