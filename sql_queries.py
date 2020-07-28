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
	brand_name VARCHAR(150) NOT NULL,
	category_id INTEGER NOT NULL,
	FOREIGN KEY (category_id) REFERENCES category(category_id)
);
""")

product_table_create = ("""
CREATE TABLE IF NOT EXISTS product
(
	product_id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
	product_name VARCHAR(200) NOT NULL,
	brand_id INTEGER NOT NULL,
	price FLOAT(2) NOT NULL,
	store_id INTEGER NOT NULL,
	rating VARCHAR(10) NOT NULL,
	offer VARCHAR(255) NOT NULL,
	FOREIGN KEY (brand_id) REFERENCES brand(brand_id)
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
INSERT INTO brand (brand_name, category_id)
SELECT DISTINCT rd.brand_name, cat.category_id
FROM raw_data AS rd, category AS cat
""")

product_table_insert = ("""
INSERT INTO product (product_name, brand_id, price, store_id, rating, offer)
SELECT rd.product_name, b.brand_id, rd.price, rd.store_id, rd.rating, rd.offer
FROM raw_data AS rd, brand as b
""")

# QUERY LISTS

drop_table_queries = [raw_data_drop, category_table_drop, store_table_drop, brand_table_drop, product_table_drop]
create_table_queries = [raw_data_create, category_table_create, store_table_create, brand_table_create, product_table_create]
load_table_queries = [raw_data_load]
insert_table_queries = [category_table_insert, store_table_insert, brand_table_insert, product_table_insert]