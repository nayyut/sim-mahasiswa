JUMLAH_MAHASISWA = 5


def baca_nim(prompt):
    while True:
        nim = input(prompt).strip()
        if nim.isascii() and nim.isdigit() and len(nim) == 10:
            return nim
        print("  NIM harus 10 digit angka.")


def baca_nama(prompt):
    while True:
        nama = input(prompt).strip()
        if nama:
            return nama
        print("  Nama tidak boleh kosong.")


def baca_angka(prompt, tipe, minimum, maksimum):
    while True:
        teks = input(prompt).strip().replace(",", ".")
        try:
            nilai = tipe(teks)
        except ValueError:
            jenis = "bilangan bulat" if tipe is int else "angka"
            print(f"  Input harus berupa {jenis}.")
            continue
        if minimum <= nilai <= maksimum:
            return nilai
        print(f"  Nilai harus antara {minimum} dan {maksimum}.")


def tentukan_status(ipk, sks):
    """Mengembalikan (status, keterangan)."""
    if ipk < 1.5:
        return "Tidak Aktif", "IPK di bawah 1.5"
    if ipk >= 2.0 and sks >= 18:
        return "Aktif", "Memenuhi syarat IPK dan SKS"
    if ipk >= 2.0:
        return "Peringatan", "SKS kurang dari 18"
    return "Peringatan", "IPK 1.5 - 1.99"


def cetak_laporan(daftar):
    garis = "=" * 84
    print("\n" + garis)
    print("LAPORAN STATUS MAHASISWA".center(84))
    print(garis)
    print(f"{'No':<3} {'NIM':<12} {'Nama':<20} {'IPK':>5} {'SKS':>4}  "
          f"{'Status':<12} Keterangan")
    print("-" * 84)

    hitung = {"Aktif": 0, "Peringatan": 0, "Tidak Aktif": 0}
    for no, m in enumerate(daftar, start=1):
        status, ket = tentukan_status(m["ipk"], m["sks"])
        hitung[status] += 1
        print(f"{no:<3} {m['nim']:<12} {m['nama'][:20]:<20} "
              f"{m['ipk']:>5.2f} {m['sks']:>4}  {status:<12} {ket}")

    print("-" * 84)
    print(f"Ringkasan: Aktif = {hitung['Aktif']}, "
          f"Peringatan = {hitung['Peringatan']}, "
          f"Tidak Aktif = {hitung['Tidak Aktif']}")
    print(garis)


def main():
    print(f"=== Input Data {JUMLAH_MAHASISWA} Mahasiswa ===")
    daftar = []
    for i in range(1, JUMLAH_MAHASISWA + 1):
        print(f"\nMahasiswa ke-{i}")
        nim = baca_nim("  NIM (10 digit)  : ")
        nama = baca_nama("  Nama            : ")
        ipk = baca_angka("  IPK (0.0 - 4.0) : ", float, 0.0, 4.0)
        sks = baca_angka("  SKS (0 - 24)    : ", int, 0, 24)
        daftar.append({"nim": nim, "nama": nama, "ipk": ipk, "sks": sks})

    cetak_laporan(daftar)


if __name__ == "__main__":
    main()