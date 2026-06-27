# AI_USAGE.md

# Registro de Uso de Inteligencia Artificial

## Información del Proyecto

* **Proyecto:** Calculadora básica en Python
* **Autor:** Francisco Solórzano
* **Fecha:** Junio 2026
* **Lenguaje:** Python 3

---

# 1. Herramienta de IA Utilizada

* **Herramienta:** ChatGPT
* **Modelo:** GPT-5.5
* **Proveedor:** OpenAI

La herramienta fue utilizada como asistente de programación para mejorar la estructura, robustez y mantenibilidad del código fuente.

---

# 2. Prompt Utilizado

El siguiente prompt fue empleado para solicitar la mejora del programa original:

> "Mejora el siguiente código, hazlo más robusto y completo."

Código proporcionado:

```python
# Solicitar números al usuario
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Realizar la suma
resultado = numero1 + numero2

# Mostrar el resultado
print("La suma es:", resultado)
```

---

# 3. Cambios Realizados

## 3.1 Implementación de funciones

Se agregaron las siguientes funciones:

* `solicitar_numero()`
* `suma()`
* `resta()`
* `multiplicacion()`
* `division()`
* `mostrar_menu()`
* `main()`

### Motivo

Permite aplicar programación modular, facilitando el mantenimiento, reutilización y ampliación del código.

---

## 3.2 Validación de entradas

Se implementó un bloque `try-except` para validar los datos ingresados por el usuario.

### Motivo

Evita que el programa finalice inesperadamente cuando el usuario ingresa texto u otros valores inválidos.

---

## 3.3 Manejo de división entre cero

Se añadió una validación dentro de la función `division()`.

### Motivo

Previene errores matemáticos y evita excepciones durante la ejecución.

---

## 3.4 Menú interactivo

Se agregó un menú con las siguientes opciones:

1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Salir

### Motivo

Permite realizar múltiples operaciones sin reiniciar el programa.

---

## 3.5 Uso de la función principal `main()`

Se incorporó:

```python
if __name__ == "__main__":
    main()
```

### Motivo

Representa una buena práctica en Python, permitiendo reutilizar el archivo como módulo si fuera necesario.

---

# 4. Beneficios Obtenidos

* Mayor robustez del programa.
* Mejor experiencia para el usuario.
* Código modular y reutilizable.
* Reducción de errores de ejecución.
* Facilidad para futuras ampliaciones.
* Aplicación de buenas prácticas de programación.

---

# 5. Participación de la IA

La inteligencia artificial actuó como una herramienta de asistencia al desarrollo, proporcionando sugerencias de mejora y recomendaciones de buenas prácticas.

Las decisiones finales sobre el diseño, implementación y aceptación de los cambios correspondieron al autor del proyecto.

---

# 6. Conclusión

El uso de herramientas de inteligencia artificial permitió mejorar significativamente la calidad del programa inicial, transformando una solución básica de suma de dos números en una calculadora modular, validada y más robusta.

La IA fue utilizada como apoyo técnico y educativo, contribuyendo al aprendizaje y a la aplicación de buenas prácticas de desarrollo de software.

---

**Autor del proyecto:** Francisco Solórzano
**Herramienta utilizada:** ChatGPT (OpenAI)
**Documento:** AI_USAGE.md 