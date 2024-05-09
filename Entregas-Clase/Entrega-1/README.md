# Ejercicios

Este repositorio contiene soluciones en Python para una serie de ejercicios de programación. Cada ejercicio está completamente especificado y resuelto de manera detallada en el código.

## Ejercicio 8: Porcentajes, IVA e inversiones

### 8.1: Calcular el precio con todos los impuestos incluidos (TII)
- **Descripción**: Calcular el precio con todos los impuestos incluidos para un precio sin impuestos y un porcentaje de IVA dado.
- **Función**: `calcular_precio_con_impuestos(precio_sin_impuestos, porcentaje_iva)`
- **Argumentos**:
  - `precio_sin_impuestos` (float): Precio sin impuestos.
  - `porcentaje_iva` (float): Porcentaje del IVA.
- **Retorno**:
  - (float): Precio con todos los impuestos incluidos (TII).

### 8.2: Calcular el importe de los intereses generados
- **Descripción**: Calcular el importe de los intereses generados por un capital invertido a un interés dado durante un tiempo dado, expresado en meses.
- **Función**: `calcular_intereses(capital, tasa_interes, tiempo_meses)`
- **Argumentos**:
  - `capital` (float): Capital invertido.
  - `tasa_interes` (float): Tasa de interés (porcentaje).
  - `tiempo_meses` (int): Tiempo en meses.
- **Retorno**:
  - (float): Importe de los intereses generados.

## Ejercicio 9: Media aritmética ponderada

### 9.1: Calcular la media aritmética
- **Descripción**: Calcular la media aritmética de tres números dados.
- **Función**: `media_aritmetica(a, b, c)`
- **Argumentos**:
  - `a`, `b`, `c` (float): Números para calcular la media aritmética.
- **Retorno**:
  - (float): Media aritmética de los tres números.

### 9.2: Calcular la media ponderada
- **Descripción**: Calcular la media ponderada de una lista de valores con sus respectivos coeficientes de ponderación.
- **Función**: `media_ponderada(valores, ponderaciones)`
- **Argumentos**:
  - `valores` (list): Lista de valores.
  - `ponderaciones` (list): Lista de coeficientes de ponderación.
- **Retorno**:
  - (float): Media ponderada de los valores.

## Ejercicio 10: Área del triángulo

### 10.1: Calcular el área con lado y altura
- **Descripción**: Calcular el área de un triángulo dado un lado y la altura relativa a este lado.
- **Función**: `area_triangulo_lado_altura(lado, altura)`
- **Argumentos**:
  - `lado` (float): Longitud del lado del triángulo.
  - `altura` (float): Altura relativa al lado del triángulo.
- **Retorno**:
  - (float): Área del triángulo.

### 10.2: Calcular el área con catetos
- **Descripción**: Calcular el área de un triángulo rectángulo dado los dos lados perpendiculares.
- **Función**: `area_triangulo_rectangulo(cateto1, cateto2)`
- **Argumentos**:
  - `cateto1`, `cateto2` (float): Longitud de los catetos del triángulo rectángulo.
- **Retorno**:
  - (float): Área del triángulo rectángulo.

## Ejercicio 11: Salario y horas extra

### 11: Calcular el importe de las horas extra
- **Descripción**: Calcular el importe de las horas extra que hay que pagar, a partir del salario mensual bruto y de la cantidad de horas extra.
- **Función**: `calcular_horas_extra(salario_bruto_mensual, horas_extra)`
- **Argumentos**:
  - `salario_bruto_mensual` (float): Salario bruto mensual del empleado.
  - `horas_extra` (int): Cantidad de horas extra trabajadas en el mes.
- **Retorno**:
  - (float): Importe de las horas extra a pagar.

## Ejercicio 12: Cuenta de depósito

### 12: Definir una cuenta básica
- **Descripción**: Definir una clase `Cuenta` para gestionar cuentas de depósito y permitir operaciones como depósitos y retiros.
- **Funcionalidades**:
  - `depositar(cantidad)`: Deposita una cantidad en la cuenta.
  - `retirar(cantidad)`: Retira una cantidad de la cuenta si hay saldo suficiente.

### 12.3: Permitir descubiertos limitados y temporales
- **Descripción**: Extender la clase `Cuenta` para permitir descubiertos limitados y temporales.
- **Funcionalidades**:
  - `retirar(cantidad)`: Permite retirar incluso si el saldo es insuficiente, hasta el límite máximo de descubierto.

## Link al repositorio
https://github.com/AlvaroSantamariaAnton/Alvaro_Santamaria-Ejercicios-Introduccion-Algoritmica.git