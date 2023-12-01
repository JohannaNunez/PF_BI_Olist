ALTER TABLE orders
ADD CONSTRAINT fk_orders_customers
FOREIGN KEY (customer_id) REFERENCES customers(id);

ALTER TABLE order_items
ADD CONSTRAINT fk_order_items_orders
FOREIGN KEY (order_id) REFERENCES orders(order_id);

ALTER TABLE order_items
ADD CONSTRAINT fk_order_items_products
FOREIGN KEY (product_id) REFERENCES products(product_id);

ALTER TABLE order_payments
ADD CONSTRAINT fk_order_payments_orders
FOREIGN KEY (order_id) REFERENCES orders(order_id);

ALTER TABLE order_reviews
ADD CONSTRAINT fk_order_reviews_orders
FOREIGN KEY (order_id) REFERENCES orders(order_id);

ALTER TABLE product_category_name_translation
ADD CONSTRAINT unique_product_category_name
UNIQUE (product_category_name);
