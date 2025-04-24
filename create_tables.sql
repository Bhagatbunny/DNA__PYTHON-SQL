CREATE TABLE dna.customers (
    customer_id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    country VARCHAR(100),
    join_date DATE,
    loyalty_points INTEGER,
    is_premium BOOLEAN,
    age INTEGER,
    gender VARCHAR(10),
    membership_years FLOAT,
    loyalty_level VARCHAR(20),
    age_group VARCHAR(20),
    new_customer BOOLEAN,
    valid_email BOOLEAN
);

customer_id, name, email, country, join_date, loyalty_points, is_premium

CREATE TABLE dna.orders (
    order_id VARCHAR(10) PRIMARY KEY,
    customer_id VARCHAR(10),
    product_id VARCHAR(10),
    quantity INTEGER,
    order_date DATE,
    delivery_status VARCHAR(20),
    payment_method VARCHAR(30),
    shipping_cost NUMERIC(6, 2),
    order_year INTEGER,
    order_month INTEGER
);

CREATE TABLE dna.products (
    product_id VARCHAR(10) PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price NUMERIC(10, 2),
    in_stock INTEGER,
    added_date DATE,
    discount_percent NUMERIC(5, 2),
    brand VARCHAR(50),
    stock INTEGER,
    is_expensive BOOLEAN
);


