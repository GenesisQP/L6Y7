use miBaseDeDatos;

db.Estudiantes.insertMany([
    { "nombre": "Juan", "edad": 20, "ciudad": "Bogotá" },
    { "nombre": "Ana", "edad": 22, "ciudad": "Medellín" },
    { "nombre": "Luis", "edad": 19, "ciudad": "Cali" },
    { "nombre": "Carlos", "edad": 23, "ciudad": "Barranquilla" },
    { "nombre": "Sofía", "edad": 25, "ciudad": "Cartagena" },
    { "nombre": "David", "edad": 21, "ciudad": "Bogotá" },
    { "nombre": "Laura", "edad": 30, "ciudad": "Medellín" },
    { "nombre": "Pedro", "edad": 27, "ciudad": "Cali" },
    { "nombre": "Marta", "edad": 29, "ciudad": "Bogotá" },
    { "nombre": "Jorge", "edad": 24, "ciudad": "Barranquilla" }
]);

db.Estudiantes.find();

db.Estudiantes.find({ "ciudad": "Bogotá" });

db.Estudiantes.find({ "edad": { $gt: 20 } });
