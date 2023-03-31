-- Create Tables
CREATE TABLE product_family (
    id_product_family     INT NOT NULL,
    product_family_handle VARCHAR(45),

    PRIMARY KEY (id_product_family)
);

CREATE TABLE product (
    id_product        INT NOT NULL,
    product_sku       VARCHAR(45),
    number_of_recipes TINYINT(1),
    number_of_meals   TINYINT(1),

    fk_product_family INT,

    PRIMARY KEY (id_product)
);

CREATE TABLE `order` (
    id_order       INT NOT NULL,
    order_number   VARCHAR(45),
    delivery_date  DATE,
    purchase_price DECIMAL(8, 2),
    created_at     DATETIME,
    updated_at     DATETIME,

    fk_subscription INT,
    fk_product      INT,

    PRIMARY KEY (id_order)
);


CREATE TABLE subscription (
    id_subscription          INT NOT NULL,
    status                   VARCHAR(45),
    created_at               DATETIME,
    updated_at               DATETIME,

    fk_customer              INT,
    fk_product_subscribed_to INT,

    PRIMARY KEY (id_subscription)
);


CREATE TABLE customer (
    id_customer INT NOT NULL,
    first_name  VARCHAR(45),
    last_name   VARCHAR(45),
    email       VARCHAR(45),
    password    VARCHAR(45),
    created_at  DATETIME,
    updated_at  DATETIME,

    PRIMARY KEY (id_customer)
);

ALTER TABLE product
ADD FOREIGN KEY (fk_product_family) REFERENCES product_family(id_product_family);

ALTER TABLE `order`
ADD FOREIGN KEY (fk_subscription) REFERENCES subscription(id_subscription);

ALTER TABLE `order`
ADD FOREIGN KEY (fk_product) REFERENCES product(id_product);

ALTER TABLE subscription
ADD FOREIGN KEY (fk_customer) REFERENCES customer(id_customer);

ALTER TABLE subscription
ADD FOREIGN KEY (fk_product_subscribed_to) REFERENCES product(id_product);


INSERT INTO product_family(id_product_family, product_family_handle)
VALUES
(1, 'classic-box'),
(2, 'notclassic-box'),
(3, 'classic-box');

INSERT INTO customer(id_customer, email)
VALUES (1, 'fancygirl83@hotmail.com'),
	(2, 'notfancygirl83@hotmail.com'),
	(3, 'fancygirl83@mail.com');

INSERT INTO product(id_product, product_sku, fk_product_family)
VALUES
(1, 'sku_1', 1),
(2, 'sku_2', 2),
(3, 'not_sku', 3);

INSERT INTO subscription(id_subscription, status, fk_customer, fk_product_subscribed_to)
VALUES
(1, 'active', 1, 1),
(2, 'paused', 1, 2),
(3, 'active', 2, 2);
(4, 'paused', 1, 3);


INSERT INTO `order`(id_order, fk_subscription)
VALUES
(1, 2),
(2, 2),
(3, 2),
(4, 4);
