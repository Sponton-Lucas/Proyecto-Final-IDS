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
