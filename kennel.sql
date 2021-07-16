CREATE TABLE `Locations` (
	`id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name` TEXT NOT NULL,
	`address` TEXT NOT NULL
);
CREATE TABLE `Customers` (
	`id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name` TEXT NOT NULL,
	`address` TEXT NOT NULL,
	`email` TEXT NOT NULL,
	`password` TEXT NOT NULL
);
CREATE TABLE `Animals` (
	`id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name` TEXT NOT NULL,
	`status` TEXT NOT NULL,
	`breed` TEXT NOT NULL,
	`customer_id` INTEGER NOT NULL,
	`location_id` INTEGER,
	FOREIGN KEY(`customer_id`) REFERENCES `Customer`(`id`),
	FOREIGN KEY(`location_id`) REFERENCES `Location`(`id`)
);
CREATE TABLE `Employees` (
	`id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name` TEXT NOT NULL,
	`address` TEXT NOT NULL,
	`location_id` INTEGER NOT NULL,
	FOREIGN KEY(`location_id`) REFERENCES `Location`(`id`)
);
--
INSERT INTO `Locations`
VALUES (
		null,
		`Nashville North`,
		`<address for Nashville North>`
	);
INSERT INTO `Locations`
VALUES (
		null,
		`Nashville South`,
		`<address for Nashville South>`
	);
INSERT INTO `Locations`
VALUES (
		null,
		`Nashville West`,
		`<address for Nashville West>`
	);
--
INSERT INTO `Employees`
VALUES (null, `Tim`, 1);
INSERT INTO `Employees`
VALUES (null, `Tom`, 2);
INSERT INTO `Employees`
VALUES (null, `Steve`, 3);
--
INSERT INTO `Customers`
VALUES (null, `Lemmy Bosco`, `123 Flower Street`);
INSERT INTO `Customers`
VALUES (null, `Ramona Ramon`, `456 Bombay Bay Lane`);
INSERT INTO `Customers`
VALUES (null, `Chuck Pachinko`, `789 Ursa Way Minor`);
INSERT INTO `Customers`
VALUES (null, `Cecilia Cabron`, `Space`);
--
INSERT INTO `Animals`
VALUES (null, `Snickers`, `Recreation`, `Labrador`, 3, 1);
INSERT INTO `Animals`
VALUES (null, `Gypsy`, `Treatment`, `Pomeranian`, 1, 2);
INSERT INTO `Animals`
VALUES (null, `Blue`, `Kennel`, `Russian Blue`, 2, 1);