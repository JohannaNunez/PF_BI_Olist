-- PostgreSQL olist_dw database creation
-- PostgreSQL version 14.4

-- ATENTION: Uncomment if the database does not yet exist
-- CREATE DATABASE olist_dw WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.UTF-8';

\connect olist_dw

SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = true;
SET xmloption = content;
SET client_min_messages = warning;

CREATE EXTENSION IF NOT EXISTS pg_trgm WITH SCHEMA public;
COMMENT ON EXTENSION pg_trgm IS 'text similarity measurement and index searching based on trigrams';

CREATE EXTENSION IF NOT EXISTS "uuid-ossp" WITH SCHEMA public;
COMMENT ON EXTENSION "uuid-ossp" IS 'support for generation of UUID datatypes';


CREATE TABLE public.orders (
    order_id UUID DEFAULT public.uuid_generate_v4() PRIMARY KEY,
    order_status VARCHAR(50),
    order_purchase_timestamp TIMESTAMP,
    order_approved_at TIMESTAMP,
    order_delivered_carrier_date TIMESTAMP,
    order_delivered_customer_date TIMESTAMP,
    order_estimated_delivery_date TIMESTAMP,
    customer_id UUID
);

CREATE TABLE public.order_payments (
    payment_id UUID DEFAULT public.uuid_generate_v4() PRIMARY KEY,
    payment_sequential INT,
    payment_type VARCHAR(255),
    payment_installments INT,
    payment_value DECIMAL(10,2),
    order_id UUID
);

CREATE TABLE public.order_reviews (
    review_unique_id UUID DEFAULT public.uuid_generate_v4() PRIMARY KEY,
    review_id UUID,
    review_score INT,
    review_creation_date TIMESTAMP,
    review_answer_timestamp TIMESTAMP,
    order_id UUID
);

CREATE TABLE public.order_items (
    item_id UUID DEFAULT public.uuid_generate_v4() PRIMARY KEY,
    order_item_id INT,
    shipping_limit_date TIMESTAMP,
    price DECIMAL(10,2),
    freight_value DECIMAL(10,2),
    order_id UUID,
    product_id UUID,
    seller_id UUID
);

CREATE TABLE public.customers (
    customer_id UUID DEFAULT public.uuid_generate_v4() PRIMARY KEY,
    customer_zip_code_prefix  VARCHAR(20) NOT NULL,
    customer_city VARCHAR(255) NOT NULL,
    customer_state VARCHAR(255) NOT NULL
);

CREATE TABLE public.products (
    product_id UUID DEFAULT public.uuid_generate_v4() PRIMARY KEY,
    product_category_name VARCHAR(255),
    product_name_length INT,
    product_description_length INT,
    product_photos_qty INT,
    product_weight_g INT,
    product_length_cm INT,
    product_height_cm INT,
    product_width_cm INT
);

CREATE TABLE public.product_category_name_translation (
    translation_id UUID DEFAULT public.uuid_generate_v4() PRIMARY KEY,
    product_category_name VARCHAR(255),
    product_category_name_english VARCHAR(255)
);

ALTER TABLE public.orders
ADD CONSTRAINT fk_orders_customers
FOREIGN KEY (customer_id) REFERENCES public.customers(customer_id);

ALTER TABLE public.order_payments
ADD CONSTRAINT fk_order_payments_orders
FOREIGN KEY (order_id) REFERENCES public.orders(order_id);

ALTER TABLE public.order_reviews
ADD CONSTRAINT fk_order_reviews_orders
FOREIGN KEY (order_id) REFERENCES public.orders(order_id);

ALTER TABLE public.order_items
ADD CONSTRAINT fk_order_items_orders
FOREIGN KEY (order_id) REFERENCES public.orders(order_id);

ALTER TABLE public.order_items
ADD CONSTRAINT fk_order_items_products
FOREIGN KEY (product_id) REFERENCES public.products(product_id);

ALTER TABLE public.product_category_name_translation
ADD CONSTRAINT unique_product_category_name
UNIQUE (product_category_name);




