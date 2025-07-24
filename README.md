
# Lab 2 - Codificación y Decodificación con Hamming (7,4)

Este laboratorio implementa un esquema de detección y corrección de errores utilizando el algoritmo de **Hamming (7,4)**.

## Estructura del Proyecto

```
Lab2-P1-Redes/
├── emisor_hamming/           # Código en Rust
│   └── src/main.rs
├── receptor_hamming/         # Código en Python
│   └── src/main.py
└── mensaje_codificado.txt    # Archivo generado por el emisor con el mensaje Hamming
```

---

## Cómo ejecutar el Emisor (Rust)

### Requisitos:

- Tener instalado `Rust` y `cargo`.

### Pasos para ejecutar:

```bash
cd emisor_hamming
cargo run
```

### Ejemplo de ejecución:

```
Ingrese el mensaje en binario (ejemplo: 1011001):
1010
Mensaje codificado en Hamming (7,4): 1011010
```

- El mensaje también se guarda en el archivo `mensaje_codificado.txt`.

---

## Cómo ejecutar el Receptor (Python)

### Requisitos:

- Tener instalado `Python 3.11` o superior

### Pasos para ejecutar:

```bash
cd receptor_hamming/src
python main.py
```

### Ejemplo de ejecución:

```
Introduce la cadena Hamming (7,4): 1011010
== Bloque #1 ==
No se detectó error.
Bloque corregido:   1011010
Datos extraídos:    1010

Mensaje final recompuesto: 1010
```
