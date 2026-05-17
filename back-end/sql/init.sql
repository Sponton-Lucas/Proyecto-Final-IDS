CREATE DATABASE IF NOT EXISTS tp_final;
USE tp_final;


#TABLAS
CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre_apellido VARCHAR(100) NOT NULL,
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
