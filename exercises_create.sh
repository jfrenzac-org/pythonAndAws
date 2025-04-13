#!/bin/bash

# Solicitar al usuario un número entre 5 y 10
read -p "Ingrese un número del 5 al 10: " num

# Validar que el número esté en el rango permitido
while ! [[ "$num" =~ ^[5-9]$|^10$ ]]; do
    echo "Entrada inválida. Debe ser un número del 5 al 10."
    read -p "Ingrese un número del 5 al 10: " num
done

# Crear los archivos con base en el número ingresado
for ((i = 1; i <= num; i++))
do
    touch "exercise_${i}.py"
done

echo "Se han creado $num archivos en el directorio actual: $(pwd)"
