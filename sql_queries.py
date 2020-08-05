# DROP TABLES

raw_data_drop = "DROP TABLE IF EXISTS raw_data;"
category_table_drop = "DROP TABLE IF EXISTS category;"
store_table_drop = "DROP TABLE IF EXISTS store;"
brand_table_drop = "DROP TABLE IF EXISTS brand;"
product_table_drop = "DROP TABLE IF EXISTS product;"

# FOREIGN KEY CHECK

foreign_key_off = "SET FOREIGN_KEY_CHECKS = 0;"
foreign_key_on = "SET FOREIGN_KEY_CHECKS = 1;"

# CREATE TABLES

raw_data_create = ("""
CREATE TABLE IF NOT EXISTS raw_data
(
	product_id INTEGER,
	product_name VARCHAR(200),
	price FLOAT(2),
	category_name VARCHAR(150),
	brand_name VARCHAR(150),
	stock VARCHAR(150),
	store_id INTEGER,
	state_abv VARCHAR(2),
	city VARCHAR(50),
	rating VARCHAR(10),
	reviews VARCHAR(20),
	offer VARCHAR(255)
);
""")

category_table_create = ("""
CREATE TABLE IF NOT EXISTS category
(
	category_id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
	category_name VARCHAR(150) NOT NULL
);
""")

store_table_create = ("""
CREATE TABLE IF NOT EXISTS store
(
	store_id INTEGER NOT NULL,
	state_abv VARCHAR(2) NOT NULL,
	city VARCHAR(50) NOT NULL
);
""")

brand_table_create = ("""
CREATE TABLE IF NOT EXISTS brand
(
	brand_id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
	brand_name VARCHAR(150) NOT NULL
);
""")

product_table_create = ("""
CREATE TABLE IF NOT EXISTS product
(
	id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
	product_id INTEGER NOT NULL,
	product_name VARCHAR(200) NOT NULL,
	price FLOAT(2) NOT NULL,
	stock VARCHAR(20) NOT NULL,
	store_id INTEGER NOT NULL,
	rating VARCHAR(10) NOT NULL,
	reviews VARCHAR(15) NOT NULL,
	offer VARCHAR(255) NOT NULL,
    brand_name VARCHAR(150),
	category_name VARCHAR(150) NOT NULL
);
""")

# LOAD TABLES

raw_data_load = ("""
INSERT INTO raw_data VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
""")

# INSERT TABLES

category_table_insert = ("""
INSERT INTO category (category_name)
SELECT DISTINCT rd.category_name
FROM raw_data AS rd
""")

store_table_insert = ("""
INSERT INTO store (store_id, state_abv, city)
SELECT DISTINCT rd.store_id, rd.state_abv, rd.city
FROM raw_data AS rd
""")

brand_table_insert = ("""
INSERT INTO brand (brand_name)
SELECT DISTINCT rd.brand_name
FROM raw_data AS rd
""")

product_table_insert = ("""
INSERT INTO product (product_id, product_name, price, stock, store_id, rating, reviews, offer, brand_name, category_name)
SELECT rd.product_id, rd.product_name, rd.price, rd.stock, rd.store_id, rd.rating, rd.reviews, rd.offer, rd.brand_name, rd.category_name
FROM raw_data AS rd;

ALTER TABLE product ADD brand_id INTEGER;
UPDATE product AS p, brand AS b
SET p.brand_id = b.brand_id
WHERE p.brand_name = b.brand_name;

ALTER table product ADD category_id INTEGER;
UPDATE product AS p, category AS cat
SET p.category_id = cat.category_id
WHERE p.category_name = cat.category_name;

ALTER TABLE product DROP brand_name;
ALTER TABLE product DROP category_name;
ALTER TABLE product ADD CONSTRAINT brand_id FOREIGN KEY (brand_id) REFERENCES brand(brand_id);
ALTER TABLE product ADD CONSTRAINT category_id FOREIGN KEY (category_id) REFERENCES category(category_id);
""")

# QUERY LISTS

drop_table_queries = [raw_data_drop, category_table_drop, store_table_drop, brand_table_drop, product_table_drop]
create_table_queries = [raw_data_create, category_table_create, store_table_create, brand_table_create, product_table_create]
load_table_queries = [raw_data_load]
insert_table_queries = [category_table_insert, store_table_insert, brand_table_insert, product_table_insert]