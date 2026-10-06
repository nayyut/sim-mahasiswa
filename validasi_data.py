import math


def validasi_nim(nim):
    errors = []
    nim = str(nim).strip()

    if not (nim.isascii() and nim.isdigit()):
        errors.append("NIM hanya boleh berisi angka (tanpa huruf, spasi, atau simbol).")
    elif len(nim) != 10:
        errors.append(f"NIM harus 10 digit (yang dimasukkan {len(nim)} digit).")
    else:
        tahun = int(nim[:4])
        if not 2000 <= tahun <= 2037:
            errors.append(f"Tahun masuk pada NIM ({tahun}) harus antara 2000 dan 2037.")
    return errors


def validasi_ipk(ipk):
    try:
        nilai = float(str(ipk).strip().replace(",", "."))
    except ValueError:
        return ["IPK harus berupa angka."]

    if math.isnan(nilai) or not 0.0 <= nilai <= 4.0:
        return ["IPK harus berada di antara 0.0 dan 4.0."]
    return []


def _validasi_bulat(nilai, nama, minimum, maksimum):
    try:
        angka = int(str(nilai).strip())
    except ValueError:
        return [f"{nama} harus berupa bilangan bulat."]

    if not minimum <= angka <= maksimum:
        return [f"{nama} harus berada di antara {minimum} dan {maksimum}."]
    return []


def validasi_sks(sks):
    return _validasi_bulat(sks, "SKS", 0, 24)


def validasi_semester(semester):
    return _validasi_bulat(semester, "Semester", 1, 14)


def validasi_mahasiswa(nim, ipk, sks, semester):
    """Menjalankan semua validasi; mengembalikan dict {field: [error, ...]}."""
    hasil = {
        "NIM": validasi_nim(nim),
        "IPK": validasi_ipk(ipk),
        "SKS": validasi_sks(sks),
        "Semester": validasi_semester(semester),
    }
    return {field: errs for field, errs in hasil.items() if errs}


def tampilkan_hasil(error_per_field):
    print("\n" + "=" * 50)
    if not error_per_field:
        print("HASIL: SEMUA DATA VALID".center(50))
    else:
        total = sum(len(e) for e in error_per_field.values())
        print(f"HASIL: DITEMUKAN {total} KESALAHAN".center(50))
        print("-" * 50)
        for field, errs in error_per_field.items():
            for e in errs:
                print(f"  [{field}] {e}")
    print("=" * 50)


def main():
    print("=== Validasi Data Mahasiswa ===")
    while True:
        print()
        nim = input("NIM (10 digit)    : ")
        ipk = input("IPK (0.0 - 4.0)   : ")
        sks = input("SKS (0 - 24)      : ")
        semester = input("Semester (1 - 14) : ")

        tampilkan_hasil(validasi_mahasiswa(nim, ipk, sks, semester))

        lagi = input("\nValidasi data lain? (y/n): ").strip().lower()
        if lagi != "y":
            print("Selesai.")
            break


if __name__ == "__main__":
    main()