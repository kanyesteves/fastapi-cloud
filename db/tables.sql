USE `volatex`;

CREATE TABLE IF NOT EXISTS `volatex`.`users` (
	`id`       INT auto_increment NOT NULL,
	`name`     VARCHAR(100) NOT NULL,
	`password` VARCHAR(100) NOT NULL,
	`office`   VARCHAR(100) NOT NULL,
	`email`    VARCHAR(100) NULL,
	CONSTRAINT `users_pk` PRIMARY KEY (`id`),
	CONSTRAINT `users_unique` UNIQUE KEY (`name`)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `volatex`.`teares` (
	`id`     INT auto_increment NOT NULL,
	`name`   VARCHAR(100) NOT NULL,
	`model`  VARCHAR(100) NOT NULL,
	`status` TINYINT(1) NOT NULL DEFAULT '0',
	CONSTRAINT `teares_pk` PRIMARY KEY (`id`),
	CONSTRAINT `teares_unique` UNIQUE KEY (`name`)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `volatex`.`order_of_operation` (
	`id`               INT auto_increment NOT NULL,
	`code`             VARCHAR(100) NOT NULL,
	`weight_per_piece` FLOAT NOT NULL,
	`total_weight`     FLOAT NOT NULL,
  `label_item` 			 TINYINT(1) NOT NULL DEFAULT '0',
	`status` 					 VARCHAR(100) NOT NULL DEFAULT 'open',
  `date_closed` 		 DATE DEFAULT NULL,
  `date_open` 		   DATE DEFAULT NULL,
	`total_pieces` 		 INT DEFAULT '0',
	`wire_porcentage`  JSON NOT NULL,
	CONSTRAINT `order_of_operation_pk` PRIMARY KEY (`id`)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

ALTER TABLE `volatex`.`order_of_operation` ADD CONSTRAINT order_of_operation_unique UNIQUE KEY (code);

CREATE TABLE IF NOT EXISTS `volatex`.`customers` (
	`id`      		INT auto_increment NOT NULL,
	`name`    		VARCHAR(100) NOT NULL,
	`description` VARCHAR(500) DEFAULT NULL,
	CONSTRAINT `customers_pk` PRIMARY KEY (`id`),
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
	CONSTRAINT `operators_pk` PRIMARY KEY (`id`)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `volatex`.`wires` (
	`id`          INT auto_increment NOT NULL,
	`name`        VARCHAR(100) NOT NULL,
	`description` VARCHAR(500) NULL,
	CONSTRAINT `wires_pk` PRIMARY KEY (`id`)
	CONSTRAINT `wires_unique` UNIQUE KEY (`name`)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `volatex`.`articles` (
	`id` 					INT auto_increment NOT NULL,
	`name` 				VARCHAR(100) NOT NULL,
	`description` VARCHAR(100) NULL,
	CONSTRAINT `articles_pk` PRIMARY KEY (`id`),
	CONSTRAINT `articles_unique` UNIQUE KEY (`name`)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `volatex`.`productions` (
	`id` 						 INT auto_increment NOT NULL,
	`code_per_piece` INT DEFAULT 0 NOT NULL,
	`weight` 				 FLOAT NOT NULL,
	`review` 				 VARCHAR(200) NOT NULL,
  `invoiced` 			 TINYINT(1) NOT NULL DEFAULT '0',
	`date` 					 DATE NOT NULL,
	`tear` 					 JSON NOT NULL,
	`op` 						 JSON NOT NULL,
	`operator` 			 JSON NOT NULL,
	CONSTRAINT `productions_pk` PRIMARY KEY (id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `volatex`.`invoicing` (
	`id` 			 				INT auto_increment NOT NULL,
	`records` 				JSON NOT NULL,
	`customer` 				VARCHAR(100) NOT NULL,
	`article`  				VARCHAR(100) NOT NULL,
	`op` 						  VARCHAR(100) NOT NULL,
	`date` 						DATE NOT NULL,
	`weight_per_wire` JSON NOT NULL,
	`total_weight` 		FLOAT NOT NULL,
	CONSTRAINT `invoicing_pk` PRIMARY KEY (id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE IF NOT EXISTS `volatex`.`groups` (
	`id` 				  INT auto_increment NOT NULL,
	`name` 			  VARCHAR(100) NOT NULL,
	`permissions` JSON NOT NULL,
	CONSTRAINT `group_pk` PRIMARY KEY (`id`)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `volatex`.`programing` (
	`id` 	 INT auto_increment NOT NULL,
	`name` VARCHAR(100) NOT NULL,
	CONSTRAINT `programing_pk` PRIMARY KEY (`id`)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;


--------- Tabelas de Relacionamento ---------

CREATE TABLE IF NOT EXISTS `volatex`.`groups_has_users` (
	`id`       INT auto_increment NOT NULL,
	`group_id` INT NOT NULL,
	`user_id`  INT NOT NULL,
	CONSTRAINT `groups_has_users_pk` PRIMARY KEY (`id`),
	CONSTRAINT `groups_has_users_groups_FK` FOREIGN KEY (`group_id`) REFERENCES `volatex`.`groups`(`id`) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT `groups_has_users_users_FK`  FOREIGN KEY (`user_id`)  REFERENCES `volatex`.`users`(`id`)  ON DELETE CASCADE ON UPDATE CASCADE
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `volatex`.`op_has_customer` (
	`id` 		      INT auto_increment NOT NULL,
	`op_id`       INT NOT NULL,
	`customer_id` INT NOT NULL,
	CONSTRAINT `op_has_customer_pk` PRIMARY KEY (`id`),
	CONSTRAINT `op_has_customer_order_of_operation_FK` FOREIGN KEY (`op_id`) REFERENCES `volatex`.`order_of_operation`(`id`) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT `op_has_customer_customers_FK`  FOREIGN KEY (`customer_id`)  REFERENCES `volatex`.`customers`(`id`)  ON DELETE CASCADE ON UPDATE CASCADE
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `volatex`.`op_has_article` (
	`id` 		     INT auto_increment NOT NULL,
	`op_id` 		 INT NOT NULL,
	`article_id` INT NOT NULL,
	CONSTRAINT `op_has_article_pk` PRIMARY KEY (`id`),
	CONSTRAINT `op_has_article_order_of_operation_FK` FOREIGN KEY (`op_id`) REFERENCES `volatex`.`order_of_operation`(`id`) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT `op_has_article_articles_FK`  FOREIGN KEY (`article_id`)  REFERENCES `volatex`.`articles`(`id`)  ON DELETE CASCADE ON UPDATE CASCADE
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `volatex`.`op_has_wires` (
	`id` 		  INT auto_increment NOT NULL,
	`op_id`   INT NOT NULL,
	`wire_id` INT NOT NULL,
	CONSTRAINT `op_has_wires_pk` PRIMARY KEY (`id`),
	CONSTRAINT `op_has_wires_order_of_operation_FK` FOREIGN KEY (`op_id`) REFERENCES `volatex`.`order_of_operation`(`id`) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT `op_has_wires_wires_FK`  FOREIGN KEY (`wire_id`)  REFERENCES `volatex`.`wires`(`id`)  ON DELETE CASCADE ON UPDATE CASCADE
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `volatex`.`programing_has_tear` (
	`id`            INT auto_increment NOT NULL,
	`programing_id` INT NOT NULL,
	`tear_id`       INT NOT NULL,
	CONSTRAINT `programing_has_tear_pk` PRIMARY KEY (`id`),
	CONSTRAINT `programing_has_tear_teares_FK` FOREIGN KEY (`tear_id`) REFERENCES `volatex`.`teares`(`id`) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT `programing_has_tear_programing_FK` FOREIGN KEY (`programing_id`) REFERENCES `volatex`.`programing`(`id`) ON DELETE CASCADE ON UPDATE CASCADE,
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `volatex`.`programing_has_op` (
	`id`            INT auto_increment NOT NULL,
	`programing_id` INT NOT NULL,
	`op_id`         INT NOT NULL,
	CONSTRAINT `programing_has_op_pk` PRIMARY KEY (`id`),
	CONSTRAINT `programing_has_op_programing_FK` FOREIGN KEY (`programing_id`) REFERENCES `volatex`.`programing`(`id`) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT `programing_has_op_order_of_operation_FK` FOREIGN KEY (`op_id`) REFERENCES `volatex`.`order_of_operation`(`id`) ON DELETE CASCADE ON UPDATE CASCADE
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;





