USE `volatex`;

CREATE TABLE IF NOT EXISTS `volatex`.`users` (
	`id`       INT auto_increment NOT NULL,
	`name`     VARCHAR(100) NOT NULL,
	`password` VARCHAR(100) NOT NULL,
	`office`   VARCHAR(100) NOT NULL,
	`email`    VARCHAR(100) NULL,
	CONSTRAINT users_pk PRIMARY KEY (`id`),
	CONSTRAINT users_unique UNIQUE KEY (`name`)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `volatex`.`teares` (
	`id`     INT auto_increment NOT NULL,
	`name`   VARCHAR(100) NOT NULL,
	`model`  VARCHAR(100) NOT NULL,
	`status` BOOL DEFAULT true NOT NULL,
	CONSTRAINT teares_pk PRIMARY KEY (`id`),
	CONSTRAINT teares_unique UNIQUE KEY (`name`)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `volatex`.`order_of_operation` (
	`id`               INT auto_increment NOT NULL,
	`code`             VARCHAR(100) NOT NULL,
	`weight_per_piece` FLOAT NOT NULL,
	`total_weight`     FLOAT NOT NULL,
  `article` 				 JSON NOT NULL,
  `wires` 					 JSON NOT NULL,
	`status` 					 VARCHAR(100) NOT NULL DEFAULT 'open',
  `date_closed` 		 DATE DEFAULT NULL,
	`total_pieces` 		 INT DEFAULT '0',
	CONSTRAINT order_of_operation_pk PRIMARY KEY (`id`)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

ALTER TABLE volatex.`order_of_operation` ADD CONSTRAINT order_of_operation_unique UNIQUE KEY (code);

CREATE TABLE IF NOT EXISTS `volatex`.`customers` (
	`id`      INT auto_increment NOT NULL,
	`name`    VARCHAR(100) NOT NULL,
	`article` JSON DEFAULT NULL,
	CONSTRAINT customers_pk PRIMARY KEY (`id`),
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

ALTER TABLE `volatex`.`order_of_operation` ADD CONSTRAINT order_of_operation_customers_FK FOREIGN KEY (`customer_id`) REFERENCES `volatex`.`customers`(`id`);

CREATE TABLE IF NOT EXISTS `volatex`.`operators` (
	`id`     INT auto_increment NOT NULL,
	`name`   VARCHAR(100) NOT NULL,
	`office` VARCHAR(100) NOT NULL,
	`turn`   VARCHAR(100) NOT NULL,
	CONSTRAINT operators_pk PRIMARY KEY (`id`)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `volatex`.`wires` (
	`id`          INT auto_increment NOT NULL,
	`name`        VARCHAR(100) NOT NULL,
	`description` VARCHAR(500) NULL,
	`percentage`  INT DEFAULT NULL,
	CONSTRAINT wires_pk PRIMARY KEY (`id`)
	CONSTRAINT wires_unique UNIQUE KEY (`name`)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `volatex`.`articles` (
	`id` 					INT auto_increment NOT NULL,
	`name` 				VARCHAR(100) NOT NULL,
	`description` VARCHAR(100) NULL,
	CONSTRAINT articles_pk PRIMARY KEY (`id`),
	CONSTRAINT articles_unique UNIQUE KEY (`name`)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;



