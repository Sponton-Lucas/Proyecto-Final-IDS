#!/bin/bash

echo "🚀 Inicializando entorno del proyecto..."

cd back-end
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate
cd ..

echo "🎉 Proyecto inicializado: entorno virtual y dependencias listas."


