#!/bin/bash

echo " Lancement du conteneur tp4-app à partir de l'image im-tp4..."
docker run -d \
    --name tp4-app \
    --network net-tp4 \
    -v "$(pwd)/TP4/srv/ " \
    -p 5000:5000 \
    im-tp4

if [ $? -eq 0 ]; then
    echo " Conteneur tp4-app lancé avec succès sur http://localhost:5000"
else
    echo " Échec du lancement du conteneur."
    exit 1
fi

