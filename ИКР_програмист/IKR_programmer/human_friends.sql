DROP DATABASE IF EXISTS human_friends;
CREATE DATABASE human_friends;
USE human_friends;
CREATE TABLE animal_classes
(
	Class_ID INT AUTO_INCREMENT PRIMARY KEY, 
	Class_name VARCHAR(30)
);
INSERT INTO animal_classes (Class_name)
VALUES ('Pets'),
('Pack animals');
-- select * from animal_classes;

CREATE TABLE pets
(
	Type_ID INT AUTO_INCREMENT PRIMARY KEY,
	Animal_class_ID INT,
    Type_name VARCHAR (30),
    FOREIGN KEY (Animal_class_ID) REFERENCES animal_classes (Class_ID) 
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

INSERT INTO pets (Animal_class_ID, Type_name)
VALUES (1, 'Dogs'),
(1, 'Cats'),  
(1, 'Hamsters'); 

CREATE TABLE pack_animals
(
	Type_ID INT AUTO_INCREMENT PRIMARY KEY,
	Animal_class_ID INT,
    Type_name VARCHAR (30),
    FOREIGN KEY (Animal_class_ID) REFERENCES animal_classes (Class_ID) 
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

INSERT INTO pack_animals (Animal_class_ID, Type_name)
VALUES (2, 'Camels'),
(2, 'Horses'),  
(2, 'Donkeys'); 
-- select * from pets;

CREATE TABLE dogs 
(       
	ID INT AUTO_INCREMENT PRIMARY KEY,
	Animal_class_ID int,
    Animal_type_ID int,
    Name VARCHAR(30), 
	Birth_date DATE,
	Skills VARCHAR(200),
	Foreign KEY (Animal_class_ID) REFERENCES animal_classes (Class_ID),
	Foreign KEY (Animal_type_id) REFERENCES pets (Type_ID)
	ON DELETE CASCADE
	ON UPDATE CASCADE
);

CREATE TABLE cats 
(       
	ID INT AUTO_INCREMENT PRIMARY KEY,
	Animal_class_ID int,
    Animal_type_ID int,
    Name VARCHAR(30), 
	Birth_date DATE,
	Skills VARCHAR(200),
	Foreign KEY (Animal_class_ID) REFERENCES animal_classes (Class_ID),
	Foreign KEY (Animal_type_id) REFERENCES pets (Type_ID)
	ON DELETE CASCADE
	ON UPDATE CASCADE
);

CREATE TABLE Hamsters 
(       
	ID INT AUTO_INCREMENT PRIMARY KEY,
	Animal_class_ID int,
    Animal_type_ID int,
    Name VARCHAR(30), 
	Birth_date DATE,
	Skills VARCHAR(200),
	Foreign KEY (Animal_class_ID) REFERENCES animal_classes (Class_ID),
	Foreign KEY (Animal_type_ID) REFERENCES pets (Type_ID)
	ON DELETE CASCADE
	ON UPDATE CASCADE
);

CREATE TABLE Camels 
(       
	ID INT AUTO_INCREMENT PRIMARY KEY,
	Animal_class_ID int,
    Animal_type_ID int,
    Name VARCHAR(30), 
	Birth_date DATE,
	Skills VARCHAR(200),
	Foreign KEY (Animal_class_ID) REFERENCES animal_classes (Class_ID),
	Foreign KEY (Animal_type_id) REFERENCES pets (Type_ID)
	ON DELETE CASCADE
	ON UPDATE CASCADE
);

CREATE TABLE Horses 
(       
	ID INT AUTO_INCREMENT PRIMARY KEY,
	Animal_class_ID int,
    Animal_type_ID int,
    Name VARCHAR(30), 
	Birth_date DATE,
	Skills VARCHAR(200),
	Foreign KEY (Animal_class_ID) REFERENCES animal_classes (Class_ID),
	Foreign KEY (Animal_type_id) REFERENCES pets (Type_ID)
	ON DELETE CASCADE
	ON UPDATE CASCADE
);

CREATE TABLE Donkeys 
(       
	ID INT AUTO_INCREMENT PRIMARY KEY,
	Animal_class_ID int,
    Animal_type_ID int,
    Name VARCHAR(30), 
	Birth_date DATE,
	Skills VARCHAR(200),
	Foreign KEY (Animal_class_ID) REFERENCES animal_classes (Class_ID),
	Foreign KEY (Animal_type_id) REFERENCES pets (Type_ID)
	ON DELETE CASCADE
	ON UPDATE CASCADE
);
INSERT INTO dogs (Animal_class_ID, Animal_type_id, Name, Birth_date, Skills)
VALUES (1, 1, 'Jack', '2022-07-12', 'Come!, Sit!, Stay!, Bite!, Sing!'),
(1, 1, 'Sharik', '2018-12-12', 'Come!, Sit!, Stay!, Bite!, Paw!, Stop/Drop it/Don’t do that!');

INSERT INTO cats (Animal_class_ID, Animal_type_id, Name, Birth_date, Skills)
VALUES (1, 2, 'Kitty', '2017-03-02', 'Jump!, Lay!, Sit!, Sleep!');

INSERT INTO hamsters (Animal_class_ID, Animal_type_id, Name, Birth_date, Skills)
VALUES (1, 3, 'Hamburger', '2023-02-10', 'Die!, Max energy!, Run!');

INSERT INTO horses (Animal_class_ID, Animal_type_id, Name, Birth_date, Skills)
VALUES (2, 2, 'Jacqulyn', '2021-07-10', 'Walk!, Trot!, Back!, Easy!');

INSERT INTO donkeys (Animal_class_ID, Animal_type_id, Name, Birth_date, Skills)
VALUES (2, 3, 'Poncho', '2022-11-11', 'Jump!, Stop talking');

INSERT INTO camels (Animal_class_ID, Animal_type_id, Name, Birth_date, Skills)
VALUES (2, 1, 'Siga', '2024-01-01', null);
-- select * from camels;

DELETE FROM camels;

CREATE TABLE horses_and_donkeys AS SELECT * FROM
    horses 
UNION SELECT 
    *
FROM
    donkeys;

CREATE TABLE young_animals AS
      SELECT Animal_class_ID, Animal_type_id, ID, Name,  
      datediff(curdate(), Birth_date) DIV 30 as 'Animal_age(month)'
      from dogs 
      WHERE datediff(curdate(), Birth_date) > 365 
            AND datediff(curdate(), Birth_date) < 1095
	UNION
    SELECT Animal_class_ID, Animal_type_id, ID, Name,  
      datediff(curdate(), Birth_date) DIV 30 as 'Animal_age(month)'
      from cats 
      WHERE datediff(curdate(), Birth_date) > 365 
            AND datediff(curdate(), Birth_date) < 1095
	UNION
    SELECT Animal_class_ID, Animal_type_id, ID, Name,  
      datediff(curdate(), Birth_date) DIV 30 as 'Animal_age(month)'
      from hamsters 
      WHERE datediff(curdate(), Birth_date) > 365 
            AND datediff(curdate(), Birth_date) < 1095
	UNION
    SELECT Animal_class_ID, Animal_type_id, ID, Name,  
      datediff(curdate(), Birth_date) DIV 30 as 'Animal_age(month)'
      from hamsters 
      WHERE datediff(curdate(), Birth_date) > 365 
            AND datediff(curdate(), Birth_date) < 1095
	UNION
    SELECT Animal_class_ID, Animal_type_id, ID, Name,  
      datediff(curdate(), Birth_date) DIV 30 as 'Animal_age(month)'
      from horses 
      WHERE datediff(curdate(), Birth_date) > 365 
            AND datediff(curdate(), Birth_date) < 1095
	UNION
    SELECT Animal_class_ID, Animal_type_id, ID, Name,  
      datediff(curdate(), Birth_date) DIV 30 as 'Animal_age(month)'
      from donkeys 
      WHERE datediff(curdate(), Birth_date) > 365 
            AND datediff(curdate(), Birth_date) < 1095
    UNION
    SELECT Animal_class_ID, Animal_type_id, ID, Name,  
      datediff(curdate(), Birth_date) DIV 30 as 'Animal_age(month)'
      from camels 
      WHERE datediff(curdate(), Birth_date) > 365 
            AND datediff(curdate(), Birth_date) < 1095;
-- select * from young_animals;
SELECT 
    CONCAT(d.Animal_class_ID,
            d.Animal_type_ID,
            d.ID) AS ID,
    t.Type_name AS Animal,
    d.Name,
    d.Birth_date,
    d.Skills
FROM
    dogs AS d
        JOIN
    pets AS t ON t.Type_ID = d.Animal_type_ID 
UNION SELECT 
    CONCAT(c.Animal_class_ID,
            c.Animal_type_ID,
            c.ID) AS ID,
    t.Type_name AS Animal,
    c.Name,
    c.Birth_date,
    c.Skills
FROM
    cats AS c
        JOIN
    pets AS t ON t.Type_ID = c.Animal_type_ID 
UNION SELECT 
    CONCAT(ham.Animal_class_ID,
            ham.Animal_type_ID,
            ham.ID) AS ID,
    t.Type_name AS Animal,
    ham.Name,
    ham.Birth_date,
    ham.Skills
FROM
    hamsters AS ham
        JOIN
    pets AS t ON t.Type_ID = ham.Animal_type_ID 
UNION SELECT 
    CONCAT(hor.Animal_class_ID,
            hor.Animal_type_ID,
            hor.ID) AS ID,
    p.Type_name AS Animal,
    hor.Name,
    hor.Birth_date,
    hor.Skills
FROM
    horses AS hor
        JOIN
    pack_animals AS p ON p.Type_ID = hor.Animal_type_ID 
UNION SELECT 
    CONCAT(don.Animal_class_ID,
            don.Animal_type_ID,
            don.ID) AS ID,
    p.Type_name AS Animal,
    don.Name,
    don.Birth_date,
    don.Skills
FROM
    donkeys AS don
        JOIN
    pack_animals AS p ON p.Type_ID = don.Animal_type_ID;