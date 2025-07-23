# Estándares que debe seguir la Persona 2 (Receptor de Hamming)

## ✅ 1. Orden de bits (estándar Hamming 7,4)

Debe asumir que los bits están organizados así en cada trama de 7 bits:

| Posición | Bit | Significado |
|----------|-----|-------------|
| 1        | P1  | Paridad 1   |
| 2        | P2  | Paridad 2   |
| 3        | D1  | Dato 1      |
| 4        | P3  | Paridad 3   |
| 5        | D2  | Dato 2      |
| 6        | D3  | Dato 3      |
| 7        | D4  | Dato 4      |

---

## ✅ 2. Bits de paridad

El receptor debe recalcular las paridades así:

- **P1** verifica posiciones: 1, 3, 5, 7 (P1, D1, D2, D4)
- **P2** verifica posiciones: 2, 3, 6, 7 (P2, D1, D3, D4)
- **P3** verifica posiciones: 4, 5, 6, 7 (P3, D2, D3, D4)

Luego, debe comparar los bits de paridad recibidos con los calculados y determinar si hay error.

---

## ✅ 3. Corrección de errores

Debe usar el **síndrome** para detectar errores:

- Si todos los bits de paridad son correctos → sin errores.
- Si hay un error → el valor binario del síndrome indica la **posición del bit con error** (de 1 a 7).
- Si encuentra un error, **debe corregirlo** (flip bit) y mostrar:
  - Trama corregida
  - Posición corregida
  - Datos extraídos (D1-D4)

---

## ✅ 4. División de entrada

Debe procesar la **cadena codificada en bloques de 7 bits** (una trama por bloque).

---

## ✅ 5. Extraer datos originales

Una vez corregida cada trama, debe extraer los bits D1, D2, D3 y D4 (posiciones 3, 5, 6, 7), y reconstruir el mensaje original binario.

---

## 📝 Ejemplo práctico

Si recibe: `1011010`

| Pos | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|-----|---|---|---|---|---|---|---|
| Bit | 1 | 0 | 1 | 1 | 0 | 1 | 0 |

- Verifica paridades.
- Si todas son correctas → extrae bits 3, 5, 6, 7 → `1 0 1 0`
- Muestra: `Mensaje correcto: 1010`

Si hay un error en un bit, por ejemplo: `1001010` (bit 2 está mal):

- Calcula paridades → encuentra error en posición 2
- Corrige → nueva trama: `1011010`
- Extrae bits → `1010`

---

## 📌 Extras recomendados

- Mostrar los pasos del proceso (errores detectados, posición, corrección).
- Validar entrada (múltiplos de 7 bits).
- Lenguaje diferente al de emisor (por ejemplo: Python, C++, Java, etc.).
