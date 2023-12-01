CREATE TABLE customers (
    id UUID PRIMARY KEY,
    unique_id UUID NOT NULL,
    zip_code_prefix INT NOT NULL,
    city VARCHAR(255) NOT NULL,
    state VARCHAR(255) NOT NULL
);

CREATE TABLE order_items (
    order_id UUID,
    order_item_id INT,
    product_id UUID,
    seller_id UUID,
    shipping_limit_date TIMESTAMP,
    price DECIMAL(10,2),
    freight_value DECIMAL(10,2),
    PRIMARY KEY (order_id, order_item_id)
);

CREATE TABLE geolocation (
    zip_code_prefix INT,
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6),
    city VARCHAR(255),
    state VARCHAR(255)
);

CREATE TABLE order_payments (
    order_id UUID,
    payment_sequential INT,
    payment_type VARCHAR(255),
    payment_installments INT,
    payment_value DECIMAL(10,2)
);

CREATE TABLE order_reviews (
    review_id UUID,
    order_id UUID,
    review_score INT,
    review_comment_title VARCHAR(255),
    review_comment_message TEXT,
    review_creation_date TIMESTAMP,
    review_answer_timestamp TIMESTAMP
);

CREATE TABLE orders (
    order_id UUID PRIMARY KEY,
    customer_id UUID,
    order_status VARCHAR(50),
    order_purchase_timestamp TIMESTAMP,
    order_approved_at TIMESTAMP NULL,
    order_delivered_carrier_date TIMESTAMP NULL,
    order_delivered_customer_date TIMESTAMP NULL,
    order_estimated_delivery_date TIMESTAMP
);

CREATE TABLE products (
    product_id UUID PRIMARY KEY,
    product_category_name VARCHAR(255),
    product_name_length INT,
    product_description_length INT,
    product_photos_qty INT,
    product_weight_g INT,
    product_length_cm INT,
    product_height_cm INT,
    product_width_cm INT
);

CREATE TABLE product_category_name_translation (
    product_category_name VARCHAR(255),
    product_category_name_english VARCHAR(255)
);