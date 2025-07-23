use std::fs::File;
use std::io::{self, Write};

fn main() {
    println!("Ingrese el mensaje en binario (ejemplo: 1011001):");

    let mut entrada = String::new();
    io::stdin().read_line(&mut entrada).expect("Error al leer entrada");
    let entrada = entrada.trim();

    if !entrada.chars().all(|c| c == '0' || c == '1') {
        println!("Error: el mensaje debe contener solo 0s y 1s.");
        return;
    }

    let mut bits: Vec<u8> = entrada.chars().map(|c| c.to_digit(2).unwrap() as u8).collect();

    while bits.len() % 4 != 0 {
        bits.push(0);
    }

    let mut trama_codificada = Vec::new();

    for bloque in bits.chunks(4) {
        let d = bloque;
        let p1 = d[0] ^ d[1] ^ d[3];
        let p2 = d[0] ^ d[2] ^ d[3];
        let p3 = d[1] ^ d[2] ^ d[3];

        // Orden estándar: P1 P2 D1 P3 D2 D3 D4
        trama_codificada.push(p1);
        trama_codificada.push(p2);
        trama_codificada.push(d[0]);
        trama_codificada.push(p3);
        trama_codificada.push(d[1]);
        trama_codificada.push(d[2]);
        trama_codificada.push(d[3]);
    }

    let salida: String = trama_codificada.iter().map(|b| b.to_string()).collect();

    // Mostrar en pantalla
    println!("Mensaje codificado en Hamming (7,4): {}", salida);

    // Guardar en archivo
    let mut archivo = File::create("mensaje_codificado.txt").expect("No se pudo crear el archivo");
    writeln!(archivo, "Mensaje codificado en Hamming (7,4): {}", salida)
        .expect("No se pudo escribir en el archivo");
}
