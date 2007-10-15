CREATE TABLE brand (
  brand_id BIGINT(13) UNSIGNED NOT NULL auto_increment,
  brand_name VARCHAR(64) NOT NULL,
  PRIMARY KEY(brand_id)
);

CREATE TABLE product(
  product_id BIGINT(13) UNSIGNED NOT NULL auto_increment,
  brand_id BIGINT(13) UNSIGNED NOT NULL,
  product_name VARCHAR(255) NOT NULL,
  product_desc TEXT,
  product_count INT(11) unsigned NOT NULL,
  PRIMARY KEY(product_id)
);
