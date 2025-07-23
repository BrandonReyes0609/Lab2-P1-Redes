# Matriz H (3×7) para comprobar las 3 sumas de paridad
H_MATRIX = [
    [1, 0, 1, 0, 1, 0, 1],  # chequeo de P1 sobre bits [0,2,4,6]
    [0, 1, 1, 0, 0, 1, 1],  # chequeo de P2 sobre bits [1,2,5,6]
    [0, 0, 0, 1, 1, 1, 1],  # chequeo de P3 sobre bits [3,4,5,6]
]

def receiver_hamming74(codeword: str) -> str:
    recovered = []
    total_blocks = len(codeword) // 7

    for blk_idx in range(total_blocks):
        # Extraemos bloque de 7 bits como lista de enteros
        start = blk_idx * 7
        block = list(map(int, codeword[start:start+7]))

        # Calcular multiplicando H_MATRIX × block (mod 2)
        syndrome = [
            sum(h_bit * block[j] for j, h_bit in enumerate(row)) % 2
            for row in H_MATRIX
        ]
        # Conversión de bits de síndrome a posición de error (1..7)
        err_pos = syndrome[0] + 2*syndrome[1] + 4*syndrome[2]

        print(f"== Bloque #{blk_idx+1} ==")
        if err_pos == 0:
            print("No se detectó error.")
        else:
            print(f"Error en posición {err_pos}, corrigiendo bit ...")
            # Corregimos invirtiendo el bit
            block[err_pos-1] ^= 1

        # Índices donde están los bits de datos D1,D2,D3,D4
        data_indices = [2, 4, 5, 6]
        data_bits = [block[i] for i in data_indices]

        print("Bloque corregido:  ", ''.join(str(b) for b in block))
        print("Datos extraídos:  ", ''.join(str(b) for b in data_bits))
        print()

        recovered.append(''.join(str(b) for b in data_bits))

    return ''.join(recovered)


if __name__ == "__main__":
    raw = input("Introduce la cadena Hamming (7,4): ").strip()
    # Validación básica
    if not raw or any(ch not in "01" for ch in raw):
        print("¡ERROR! Solo se admiten caracteres '0' y '1'.")
        exit(1)

    # Asegurar longitud múltiplo de 7 añadiendo padding al final
    rem = len(raw) % 7
    if rem != 0:
        extra = 7 - rem
        print(f"Longitud no múltiplo de 7: añado {extra} ceros de relleno.")
        raw += "0" * extra

    resultado = receiver_hamming74(raw)
    print("Mensaje final recompuesto:", resultado)
