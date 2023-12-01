CREATE TABLE postal_codes (
    zip_code_prefix INT PRIMARY KEY,
    city VARCHAR(255) NOT NULL,
    state VARCHAR(255) NOT NULL
);

-- Insertar códigos postales únicos en postal_codes desde customers
INSERT INTO postal_codes (zip_code_prefix, city, state)
SELECT zip_code_prefix, city, state
FROM (
    SELECT zip_code_prefix, city, state, ROW_NUMBER() OVER (PARTITION BY zip_code_prefix ORDER BY id) as row_num
    FROM customers
) AS subquery
WHERE row_num = 1
AND NOT EXISTS (
    SELECT 1 FROM postal_codes WHERE zip_code_prefix = subquery.zip_code_prefix
);

ALTER TABLE customers
DROP COLUMN city,
DROP COLUMN state;

ALTER TABLE geolocation
DROP COLUMN city,
DROP COLUMN state;

INSERT INTO postal_codes (zip_code_prefix, city, state)
SELECT g.zip_code_prefix, 'Desconocida', 'Desconocido'
FROM geolocation g
WHERE NOT EXISTS (
    SELECT 1 FROM postal_codes p WHERE p.zip_code_prefix = g.zip_code_prefix
)
GROUP BY g.zip_code_prefix;

-- Relación entre customers y postal_codes
ALTER TABLE customers
ADD CONSTRAINT fk_customers_postal_codes
FOREIGN KEY (zip_code_prefix) REFERENCES postal_codes(zip_code_prefix);

-- Relación entre geolocation y postal_codes
ALTER TABLE geolocation
ADD CONSTRAINT fk_geolocation_postal_codes
FOREIGN KEY (zip_code_prefix) REFERENCES postal_codes(zip_code_prefix);


