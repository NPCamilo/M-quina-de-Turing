# Simulador de Máquina de Turing - UTP

Este proyecto es un simulador interactivo de Máquinas de Turing (MT) desarrollado para la asignatura de Teoría de la Computación de la Universidad Tecnológica de Pereira (UTP). Permite cargar definiciones formales, visualizar el movimiento de la cinta y ejecutar algoritmos paso a paso.

## 🚀 Características
- **Carga de Archivos .mt**: Intérprete de definiciones formales de máquinas.
- **Visualización Dinámica**: Interfaz web que muestra la cinta, el estado actual y la posición de la cabeza.
- **Control de Simulación**: Modos "Paso a paso" y "Ejecución Completa".
- **Historial de Pasos**: Contador de transiciones realizadas.

## 🛠️ Requisitos e Instalación
El proyecto está desarrollado en Python utilizando el framework Django.

1. Clonar el repositorio:
   git clone https://github.com/tu-usuario/simulador-mt-utp.git

2. Instalar las dependencias:
   pip install django

3. Ejecutar el servidor:
   python manage.py runserver

4. Abrir en el navegador:
   http://127.0.0.1:8000

## 📂 Formato de los Archivos .mt
Para que el simulador reconozca una máquina, el archivo de texto debe seguir esta estructura:

Estados: q0, q1, qf
Alfabeto_entrada: 0, 1
Alfabeto_cinta: 0, 1, B
Inicial: q0
Finales: qf
Blanco: B
Transiciones:
q0,0 -> q1,B,R
q1,1 -> qf,1,S

### Convenciones de Transición:
- L: Mover a la izquierda (Left)
- R: Mover a la derecha (Right)
- S: Permanecer en el sitio (Stay)

## 📝 Algoritmos Implementados (Guía de Uso)

### 1. Duplicadora Binaria (w → w#w)
Copia la cadena de entrada al final de la cinta con un separador '#'.
- **Entrada sugerida:** `101`
- **Resultado esperado:** `101#101`

### 2. Suma de Números en Unario (1ⁿ # 1ᵐ → 1ⁿ⁺ᵐ)
Realiza la suma aritmética de dos bloques de unos.
- **Entrada sugerida:** `11#111`
- **Resultado esperado:** `11111`

### 3. Reconocimiento de Palíndromos
Determina si una cadena es igual al derecho y al revés.
- **Entrada sugerida:** `1001`
- **Resultado esperado:** Estado ACEPTADO.

### 4. Lenguaje 0ⁿ1ⁿ
Verifica que la cantidad de ceros sea igual a la de unos y que estén en orden.
- **Entrada sugerida:** `000111`
- **Resultado esperado:** Estado ACEPTADO.

## 📁 Estructura del Código
- `parser.py`: Clase encargada de procesar y validar los archivos de texto.
- `turing_machine.py`: Motor lógico que gestiona la cinta y las transiciones.
- `views.py`: Controlador de Django que maneja el estado de la simulación.
- `templates/`: Archivos HTML para la interfaz de usuario.

---
Proyecto desarrollado por estudiantes de Ingeniería de Sistemas y Computación - UTP.
