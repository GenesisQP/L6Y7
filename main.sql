CREATE TABLE Estudiantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(50),
    edad INT,
    ciudad VARCHAR(50)
);

INSERT INTO Estudiantes (nombre, edad, ciudad)
VALUES
    ('Ana Pérez', 22, 'Madrid'),
    ('Luis García', 19, 'Barcelona'),
    ('Pedro Sánchez', 24, 'Madrid'),
    ('Marta Rodríguez', 30, 'Valencia'),
    ('Laura Gómez', 18, 'Barcelona');

SELECT * FROM Estudiantes;

SELECT * FROM Estudiantes
WHERE ciudad = 'Barcelona';

SELECT * FROM Estudiantes
WHERE edad > 20;


