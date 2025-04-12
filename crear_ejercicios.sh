#!/bin/bash

# Crear los 10 archivos en el directorio actual
for i in {1..10}
do
    touch "exercise_${i}.py"
done

echo "Archivos creados en el directorio actual: $(pwd)"
