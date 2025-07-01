#  Generador de Contraseñas seguras

Este proyecto permite generar contraseñas seguras de manera manual o automática, incluyendo opciones como:
- Contraseñas fáciles de leer
- Contraseñas fáciles de decir
- Contraseñas con todos los tipos de caracteres (mayúsculas, minúsculas, números y símbolos)

También evalúa el nivel de seguridad de cada contraseña generada.

---

##  ¿Cómo se ejecuta?

1. Se debe tener **Python 3.10** o superior instalado.
2. Descarga el archivo `proyecto-final-generador-contrasenas-kassandra-Proanio` 
3. Abrir una terminal en la carpeta del proyecto.
4. Ejecuta el archivo con:

```bash
python proyecto-final-generador-contrasenas-kassandra-Proanio.py
```

---

##  Librerías utilizadas

Este proyecto utiliza las siguientes librerías:

- `random` ✅ (librería estándar de Python)
- `string` ✅ (librería estándar de Python)
- `re` ✅ (librería estándar de Python)


 No se necesita instalar nada extra, porque todo es parte de Python estándar.

---

##  Requisitos

- Python 3.10 o superior
- Editor de código (Visual Studio Code, PyCharm, etc.)

---

##  Estructura del proyecto

```
/proyecto-final-generador-contrasenas-kassandra-proanio/
│
├── generador_de_contrasenas.py      # Código principal
├── README.md                         # Este archivo
├── diagramas/
│   ├── diagrama1_menu_principal.png
│   ├── diagrama2_submenu.png
│   ├── diagrama3_generar contraseña.png
│   ├── diagrama4_contraseña personalizada.png
│   └── diagrama5.png
```

---

##  ¿Cómo está organizado el código?

- Primero se muestra un **menú principal** donde el usuario elige entre contraseña manual o automática.
- Si elige automática, se permite seleccionar el tipo de contraseña.
- Luego se genera la contraseña y se evalúa su nivel de seguridad.
- Se muestran mensajes claros al usuario y se valida cada input.
- El código está modularizado en funciones según los diagramas de flujo.

---

##  Diagramas de flujo

Todos los diagramas que explican el funcionamiento del código están en la carpeta `/diagramas`.

---

##  Autor

Kassandra Proaño – Proyecto final generador contrasenas
