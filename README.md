# Proyecto Final IDS - Sistema de Reservas de Restaurante

Aplicación web desarrollada en Flask que gestiona reservas, usuarios y menú  de un restaurante.
El proyecto está dividido en dos módulos:

- Back-end: API REST con conexión a MySql.
- Front-end: Interfaz Flask que consume la API y muestra el menú, reservas , reseñas, etc.

## 🚀 Instalación y configuración

1. **Clonar el repositorio**
```bash
git clone https://github.com/Sponton-Lucas/Proyecto-Final-IDS.git
cd proyecto-final-ids
```

2. **Crear usuario y base de datos en MySql**
```sql
CREATE USER IF NOT EXISTS 'caidaSiu'@'localhost' IDENTIFIED BY '1234';
CREATE DATABASE restaurante_db;
GRANT ALL PRIVILEGES ON restaurante_db.* TO 'caidaSiu'@'localhost';
FLUSH PRIVILEGES;
```

3. **Iinicializar entorno y dependencias**
```bash
bash init.sh
```
Esto crea los entornos virtuales e instala todas las dependencias del requirements.txt en cada módulo.

4. **Ejecutar script SQL**
```bash
mysql -u <nombre_usuario> -p restaurante_db < back-end/sql/init.sql
```
(Cambiar nombre_usuario por su respectivo usuario en MySql)

## 🧠 Ejecución del proyecto

**Back-end**
```bash
cd back-end
source venv/bin/activate
python3 app.py
```
Servidor disponible en http://127.0.0.1:5000.

**Front-end**
```bash
cd front-end
source venv/bin/activate
python3 app.py
```
Interfaz disponible en http://127.0.0.1:3000.

## 📌 Endpoints principales

### Usuarios
- **GET /usuarios** → Listar todos los usuarios
- **POST /usuarios** → Crear un nuevo usuario
- **PUT /usuarios/{id}** → Reemplazar datos de un usuario
- **PATCH /usuarios/{id}** → Actualizar parcialmente un usuario
- **DELETE /usuarios/{id}** → Eliminar un usuario

### Servicios Extra
- **GET /servicios_extra**
- **POST /servicios_extra**
- **PUT /servicios_extra/{id}**
- **PATCH /servicios_extra/{id}**
- **DELETE /servicios_extra/{id}**

### Reseñas
- **GET /resenas**
- **POST /resenas**
- **PUT /resenas/{id}**
- **PATCH /resenas/{id}**
- **DELETE /resenas/{id}**

### Postres
- **GET /postres**
- **POST /postres**
- **PUT /postres/{id}**
- **PATCH /postres/{id}**
- **DELETE /postres/{id}**

### Bebidas
- **GET /bebidas**
- **POST /bebidas**
- **PUT /bebidas/{id}**
- **PATCH /bebidas/{id}**
- **DELETE /bebidas/{id}**

### Comida Principal
- **GET /comida_principal**
- **POST /comida_principal**
- **PUT /comida_principal/{id}**
- **PATCH /comida_principal/{id}**
- **DELETE /comida_principal/{id}**

### Reservas
- **GET /reservas**
- **POST /reservas**
- **PUT /reservas/{id}**
- **PATCH /reservas/{id}**
- **DELETE /reservas/{id}**

## 🧰 Dependencias principales

- Flask 3.1.3
- Flask-Mail 0.10.0
- mysql-connector-python 9.7.0
- python-dotenv 1.2.2
- bcrypt 5.0.0
- Jinja2 3.1.6
- Werkzeug 3.1.8


## 💡 Créditos

Proyecto desarrollado por Grupo **caidaSiu**

**Integrantes:**

- Lucas Sponton
- Mia Torres
- Ivan Nolasco
- Thomas Alabart
- Sofia Ramirez
- Agustin Antonic
- Silvana Romero
- Alejandro Daniel Pinto
- Jose Antonio Rivas























# ¡Proyecto-Final-IDS!
# Restaurante App


## 🚀 Instalación rápida

### 1. Clonar el repositorio
```bash
git clone <URL_DEL_REPO>
cd <NOMBRE_DEL_REPO>
```

### 2. Crear la base de datos

mysql -u <usuario_mysql> -p < back-end/sql/init.sql
( Reemplazá <usuario_mysql> por tu usuario de MySQL (ej: root o el que creaste).)

### 3. Crear usuario de mySql

CREATE USER IF NOT EXISTS 'caidaSiu'@'localhost' IDENTIFIED BY '1234';
GRANT ALL PRIVILEGES ON restaurante_db.* TO 'caidaSiu'@'localhost';
FLUSH PRIVILEGES;

### 4. Inicializar entornos virtuales
./init.sh
(Esto crea los entornos en back-end/venv y front-end/venv e instala dependencias.)

### 5. Levantar el back-end
cd back-end
source venv/bin/activate
flask run

### 6. Levantar el front-end
cd front-end
source venv/bin/activate
flask run


