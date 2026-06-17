CREATE DATABASE IF NOT EXISTS restaurante_db;
USE restaurante_db;


#TABLAS
CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre_apellido VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    telefono VARCHAR(20) NOT NULL,
    contrasenia VARCHAR(100) NOT NULL,
    es_admin BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS servicios_extra (
    id_servicio INT AUTO_INCREMENT PRIMARY KEY,
    nombre_servicio VARCHAR(100) NOT NULL,
    precio INT DEFAULT 0
);

CREATE TABLE IF NOT EXISTS resenas (
    id_resenas INT AUTO_INCREMENT PRIMARY KEY,
    mensaje VARCHAR(200),
    usuario_id INT,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id_usuario) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS postres (
    id_postre INT AUTO_INCREMENT PRIMARY KEY,
    precio INT DEFAULT 0,
    nombre VARCHAR(50) NOT NULL,
    es_vegano BOOLEAN DEFAULT FALSE,
    es_celiaco BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS bebidas (
    id_bebidas INT AUTO_INCREMENT PRIMARY KEY,
    precio INT DEFAULT 0,
    nombre VARCHAR(50) NOT NULL,
    es_alcoholica BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS comida_principal (
    id_plato INT AUTO_INCREMENT PRIMARY KEY,
    nombre_plato VARCHAR(100) NOT NULL, 
    precio INT DEFAULT 0, 
    es_vegano BOOLEAN DEFAULT FALSE,
    es_celiaco BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS reservas (
    id_reservas INT AUTO_INCREMENT PRIMARY KEY,
    token VARCHAR(255) UNIQUE NOT NULL,
    usuario_id INT NOT NULL,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    cantidad_personas INT NOT NULL,
    estado VARCHAR(20) DEFAULT 'pendiente',
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id_usuario) ON DELETE CASCADE
);

INSERT INTO usuarios (id_usuario, nombre_apellido, email, telefono, contrasenia, es_admin)
VALUES (1, 'Admin', 'admin@gmail.com', '1234567890', '$2b$12$S.q7K65PcCVxJ3sztawZ6.8uOlwhHrhABAIGdpvFUXs1rBbu26aha', TRUE);

