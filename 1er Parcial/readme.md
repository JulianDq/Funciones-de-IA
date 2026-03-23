# 1er Parcial - Ejercicios Básicos de Python con Tkinter

Esta carpeta contiene la solución a los 10 ejercicios planteados para el primer parcial, implementados completamente en Python con una interfaz gráfica basada en `tkinter`.

## Estructura del Proyecto

El sistema está diseñado de manera modular para separar la interfaz gráfica principal de la lógica de cada ejercicio individual:

- **`login.py`**: Es el punto de entrada a la aplicación. Presenta una interfaz de inicio de sesión.
  - **Usuario:** `admin`
  - **Contraseña:** `1234`
- **`ventana_principal.py`**: Contiene el menú principal del sistema. Funciona como un "dashboard" desde el cual se pueden ejecutar, mediante botones, cada uno de los 10 ejercicios en ventanas independientes.
- **Carpeta `ejercicios/`**: Contiene los 10 módulos (`ejercicio_1.py` hasta `ejercicio_10.py`). Cada archivo maneja la ventana (`Toplevel`) y la lógica exclusiva de ese problema (cálculos, validaciones e historiales).

## Lista de Ejercicios Implementados

1. **Aumento de Sueldo:** Calcula el 8% de aumento para trabajadores con sueldo menor a 7000 e incluye historial.
2. **Parque de Diversiones:** Sistema de tickets y descuentos por edad (menores de 10: 25%, 10 a 17: 10%). Muestra reporte de recaudación.
3. **Descuentos por Mes:** Sistema de compras que aplica descuentos en Octubre (15%), Diciembre (20%) y Julio (10%).
4. **Validar Número (< 10):** Valida la entrada repetitiva de números y cuenta los intentos fallidos.
5. **Validar Rango (0, 20):** Similar al anterior, validando que el número pertenezca a un rango específico.
6. **Historial de Validaciones:** Expande el Ejercicio 5 guardando en una lista todos los intentos (correctos e incorrectos) y mostrando el historial completo.
7. **Suma de Enteros:** Suma consecutiva de los primeros `n` números enteros positivos mostrando la secuencia completa.
8. **Suma Acumulativa:** Ingreso continuo de números, que va mostrando la suma total y se detiene automáticamente al ingresar un `0`.
9. **Suma Límite:** Ingreso continuo de números que se detiene cuando la suma acumulada histórica supera los `100`.
10. **Pago de Trabajadores:** Cálculo de horas normales, horas extras (50% valor normal) y bonificaciones por cantidad de hijos.

## Cómo Ejecutarlo

1. Abre tu terminal o consola de comandos.
2. Posiciónate en la carpeta del primer parcial: `cd "1er Parcial"`
3. Ejecuta el archivo de login: `python login.py`
4. Ingresa las credenciales (`admin` / `1234`) y usa el menú para interactuar con las herramientas.
