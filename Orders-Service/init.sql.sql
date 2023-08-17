DROP DATABASE IF EXISTS "SOACourse";

CREATE DATABASE "SOACourse"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

CREATE TABLE carts (
   cart_id serial PRIMARY KEY,
   user_id VARCHAR ( 50 ) UNIQUE NOT NULL
);
CREATE TABLE cart_items (
   cart_item_id serial,
   cart_id INTEGER REFERENCES carts(cart_id) ON DELETE CASCADE,
   product_id VARCHAR ( 50 ) NOT NULL,
   quantity INTEGER  NOT NULL,
   amount NUMERIC NOT NULL,
   PRIMARY KEY (product_id, cart_item_id)
);


