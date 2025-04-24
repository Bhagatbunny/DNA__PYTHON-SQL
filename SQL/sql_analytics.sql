SET search_path TO dna;
-- Get the names and emails of all premium customers who joined in or after 2022.
SELECT name, email from dna.customers
WHERE is_Premium = True and EXTRACT(YEAR from Join_date) >= 2022;

-- List all orders with the customer’s name and product name. Include only orders with quantity greater than 2.
SELECT c.name, p.product_name FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN products p ON o.product_id = p.product_id
WHERE o.quantity > 2;

-- How many total loyalty points do customers from 'India' have, grouped by loyalty level?
SET search_path TO dna;
SELECT loyalty_level, SUM(loyalty_points) AS total_loyalty_points from customers
-- where country = 'Belgium'
GROUP BY loyalty_level;

-- Show each customer’s name and a label “High”, “Medium”, or “Low” based on their loyalty points:
-- High: 1000+, Medium: 500–999, Low: <500
SET search_path TO dna;
SELECT name, CASE
WHEN loyalty_points > 1000 THEN 'High'
WHEN loyalty_points between 500 and 999 THEN 'Medium'
WHEN loyalty_points < 500 THEN 'Low'
END AS loyalty_label
FROM customers;

-- Find the top 3 most expensive products (by price) in each category.
SET search_path TO dna;
SELECT product_name, category, price from products
WHERE price IN ( SELECT price from products ORDER by price DESC LIMIT 3)
ORDER by price;

-- What is the total quantity of products ordered by each customer in 2023?
total_ quantity = SUM(qunatity) as total_qi=uanity
SELECT c.customer_id, SUM(o.quantity) AS total_quantity from customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE EXTRACT(YEAR FROM o.order_date) = 2023
GROUP BY c.customer_id;

-- What is the highest-priced product for each category?
WITH CTE AS(
SELECT category, MAX(price) as max_price from products
GROUP BY category)

SELECT p.category, p.product_name from products p
JOIN CTE c ON p.price= c.max_price and p.category = c.category;

-- Write a query to fetch the most expensive product(s) in each category using RANK() or ROW_NUMBER() instead of a CTE.
WITH ranked_products as (SELECT category, product_name, price,
	ROW_NUMBER() OVER (partition by category order by price DESC) as rn 
	FROM products)
SELECT * FROM ranked_products
where rn =1;


-- will add more analytics




















