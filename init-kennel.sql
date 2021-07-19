DROP TABLE `Location`;
DROP TABLE `Customer`;
DROP TABLE `Animal`;
DROP TABLE `Employee`;
CREATE TABLE `Location` (
	`id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name` TEXT NOT NULL,
	`address` TEXT NOT NULL
);
CREATE TABLE `Customer` (
	`id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name` TEXT NOT NULL,
	`address` TEXT NOT NULL,
	`email` TEXT NOT NULL,
	`password` TEXT NOT NULL
);
CREATE TABLE `Animal` (
	`id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name` TEXT NOT NULL,
	`status` TEXT NOT NULL,
	`breed` TEXT NOT NULL,
	`customer_id` INTEGER NOT NULL,
	`location_id` INTEGER,
	FOREIGN KEY(`customer_id`) REFERENCES `Customer`(`id`),
	FOREIGN KEY(`location_id`) REFERENCES `Location`(`id`)
);
CREATE TABLE `Employee` (
	`id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name` TEXT NOT NULL,
	`address` TEXT NOT NULL,
	`location_id` INTEGER NOT NULL,
	FOREIGN KEY(`location_id`) REFERENCES `Location`(`id`)
);
--
INSERT INTO `Location`
VALUES (
		null,
		'Nashville North',
		'...address for Nashville North...'
	);
INSERT INTO `Location`
VALUES (
		null,
		'Nashville South',
		'...address for Nashville South...'
	);
INSERT INTO `Location`
VALUES (
		null,
		'Nashville West',
		'...address for Nashville West...'
	);
--
INSERT INTO `Employee`
VALUES (null, 'Tim', "Tim's House", 1);
INSERT INTO `Employee`
VALUES (null, 'Tom', "Tom's House", 2);
INSERT INTO `Employee`
VALUES (null, 'Steve', "Steve's House", 3);
--
INSERT INTO `Customer`
VALUES (
		null,
		'Lemmy Bosco',
		'123 Flower Street',
		'lemmy@bosco.com',
		'lbosco'
	);
INSERT INTO `Customer`
VALUES (
		null,
		'Ramona Ramon',
		'456 Bombay Bay Lane',
		'ramona@ramon.com',
		'rramon'
	);
INSERT INTO `Customer`
VALUES (
		null,
		'Chuck Pachinko',
		'789 Ursa Way Minor',
		'chuck@pachinko.com',
		'cpachinko'
	);
INSERT INTO `Customer`
VALUES (
		null,
		'Cecilia Cabron',
		'Space',
		'cecilia@cabron.com',
		'ccabron'
	);
--
INSERT INTO `Animal`
VALUES (null, 'Snickers', 'Recreation', 'Labrador', 3, 1);
INSERT INTO `Animal`
VALUES (null, 'Gypsy', 'Treatment', 'Pomeranian', 1, 2);
INSERT INTO `Animal`
VALUES (null, 'Blue', 'Kennel', 'Russian Blue', 2, 1);