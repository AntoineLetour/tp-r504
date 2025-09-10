#!/bin/bash

echo "Construction de l'image Docker 'im-tp4' à partir de 'Dockerfile1'..."

docker build -f Dockerfile1 -t im-tp4 .

if [ $? -eq 0 ]; then
    echo "✅ Image im-tp4 construite avec succès."
else
    echo "❌ Erreur lors de la construction de l'image im-tp4."
    exit 1
fi

