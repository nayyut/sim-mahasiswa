def rupiah(angka):
    return "Rp" + f"{angka:,.0f}".replace(",", ".")


def baca_teks(prompt):
    while True:
        teks = input(prompt).strip()
        if teks:
            return teks
        print("  Isian tidak boleh kosong.")


def baca_nim(prompt):
    while True:
        nim = input(prompt).strip()
        if nim.isascii() and nim.isdigit() and len(nim) == 10:
            return nim
        print("  NIM harus 10 digit angka.")


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


def baca_rupiah(prompt):
    while True:
        teks = input(prompt).strip().replace(".", "").replace(",", ".")
        try:
            nilai = float(teks)
        except ValueError:
            print("  Masukkan angka saja, contoh: 5000000")
            continue
        if nilai > 0:
            return nilai
        print("  Nilai harus lebih dari 0.")


def baca_ya_tidak(prompt):
    while True:
        jawab = input(prompt).strip().lower()
        if jawab in ("y", "n"):
            return jawab == "y"
        print("  Jawab dengan 'y' atau 'n'.")


# =====================================================================
# Menu 1 - Status mahasiswa
# =====================================================================

def tentukan_status(ipk, sks):
    if ipk < 1.5:
        return "Tidak Aktif", "IPK di bawah 1.5"
    if ipk >= 2.0 and sks >= 18:
        return "Aktif", "Memenuhi syarat IPK dan SKS"
    if ipk >= 2.0:
        return "Peringatan", "SKS kurang dari 18"
    return "Peringatan", "IPK 1.5 - 1.99"


def menu_status_mahasiswa():
    print("\n--- CEK STATUS MAHASISWA ---")
    jumlah = baca_angka("Jumlah mahasiswa yang diinput (1-20): ", int, 1, 20)

    daftar = []
    for i in range(1, jumlah + 1):
        print(f"\nMahasiswa ke-{i}")
        nim = baca_nim("  NIM (10 digit)  : ")
        nama = baca_teks("  Nama            : ")
        ipk = baca_angka("  IPK (0.0 - 4.0) : ", float, 0.0, 4.0)
        sks = baca_angka("  SKS (0 - 24)    : ", int, 0, 24)
        daftar.append((nim, nama, ipk, sks))

    print("\n" + "=" * 84)
    print(f"{'No':<3} {'NIM':<12} {'Nama':<20} {'IPK':>5} {'SKS':>4}  "
          f"{'Status':<12} Keterangan")
    print("-" * 84)
    hitung = {"Aktif": 0, "Peringatan": 0, "Tidak Aktif": 0}
    for no, (nim, nama, ipk, sks) in enumerate(daftar, start=1):
        status, ket = tentukan_status(ipk, sks)
        hitung[status] += 1
        print(f"{no:<3} {nim:<12} {nama[:20]:<20} {ipk:>5.2f} {sks:>4}  "
              f"{status:<12} {ket}")
    print("-" * 84)
    print(f"Ringkasan: Aktif = {hitung['Aktif']}, "
          f"Peringatan = {hitung['Peringatan']}, "
          f"Tidak Aktif = {hitung['Tidak Aktif']}")
    print("=" * 84)


# =====================================================================
# Menu 2 - Diskon biaya
# =====================================================================

def hitung_diskon(spp, anak_karyawan, ipk, tepat_waktu):
    rincian = []
    if anak_karyawan:
        rincian.append(("Anak karyawan", 25))
    if ipk >= 3.8:
        rincian.append(("Prestasi IPK >= 3.8", 20))
    elif ipk >= 3.5:
        rincian.append(("Prestasi IPK >= 3.5", 15))
    elif ipk >= 3.0:
        rincian.append(("Prestasi IPK >= 3.0", 10))
    if tepat_waktu:
        rincian.append(("Pembayaran tepat waktu", 5))

    total_persen = sum(p for _, p in rincian)
    potongan = spp * total_persen / 100
    return rincian, total_persen, potongan, spp - potongan


def menu_diskon_biaya():
    print("\n--- HITUNG DISKON BIAYA KULIAH ---")
    spp = baca_rupiah("Biaya SPP (Rp)                : ")
    anak_karyawan = baca_ya_tidak("Anak karyawan? (y/n)          : ")
    ipk = baca_angka("IPK (0.0 - 4.0)               : ", float, 0.0, 4.0)
    tepat_waktu = baca_ya_tidak("Bayar tepat waktu? (y/n)      : ")

    rincian, total_persen, potongan, final = hitung_diskon(
        spp, anak_karyawan, ipk, tepat_waktu)

    print("\n" + "=" * 46)
    if rincian:
        for nama, persen in rincian:
            print(f"  {nama:<30} {persen:>3}%")
    else:
        print("  Tidak ada diskon yang berlaku.")
    print("-" * 46)
    print(f"  {'Total diskon':<22} {total_persen:>3}%")
    print(f"  {'Biaya SPP':<22} {rupiah(spp):>20}")
    print(f"  {'Potongan':<22} {rupiah(potongan):>20}")
    print(f"  {'Biaya final':<22} {rupiah(final):>20}")
    print("=" * 46)


# =====================================================================
# Menu 3 - Peringatan stok
# =====================================================================

INVENTARIS = [
    {"nama": "Kertas A4 (rim)",   "stok": 120, "stok_minimum": 50, "harga": 55000},
    {"nama": "Tinta Printer",     "stok": 18,  "stok_minimum": 20, "harga": 95000},
    {"nama": "Spidol Whiteboard", "stok": 8,   "stok_minimum": 30, "harga": 12000},
    {"nama": "Map Folder",        "stok": 0,   "stok_minimum": 40, "harga": 3500},
    {"nama": "Baterai AA",        "stok": 45,  "stok_minimum": 40, "harga": 8000},
    {"nama": "Lakban",            "stok": 20,  "stok_minimum": 25, "harga": 9000},
    {"nama": "Penghapus Papan",   "stok": 0,   "stok_minimum": 15, "harga": 15000},
    {"nama": "Stapler",           "stok": 35,  "stok_minimum": 10, "harga": 28000},
    {"nama": "Flashdisk 32GB",    "stok": 6,   "stok_minimum": 15, "harga": 70000},
    {"nama": "Kabel HDMI",        "stok": 14,  "stok_minimum": 20, "harga": 45000},
]

LABEL_PRIORITAS = {1: "Kritis", 2: "Tinggi", 3: "Sedang", 4: "-"}


def evaluasi_item(item):
    stok, minimum = item["stok"], item["stok_minimum"]
    if stok == 0:
        return "HABIS", 1
    if stok <= minimum * 0.5:
        return "RENDAH", 2
    if stok <= minimum:
        return "PERINGATAN", 3
    return "AMAN", 4


def cetak_laporan_stok(inventaris):
    hasil = []
    for item in inventaris:
        status, prioritas = evaluasi_item(item)
        hasil.append({
            **item,
            "status": status,
            "prioritas": prioritas,
            "nilai": item["stok"] * item["harga"],
            "restock": (max(0, item["stok_minimum"] * 2 - item["stok"])
                        if status != "AMAN" else 0),
        })
    hasil.sort(key=lambda x: (x["prioritas"], x["nama"]))

    lebar = 98
    print("\n" + "=" * lebar)
    print(f"{'No':<3} {'Nama Barang':<20} {'Stok':>5} {'Min':>5} {'Status':<11} "
          f"{'Prioritas':<9} {'Nilai Stok':>14} {'Restock':>8}")
    print("-" * lebar)
    for no, h in enumerate(hasil, start=1):
        print(f"{no:<3} {h['nama']:<20} {h['stok']:>5} {h['stok_minimum']:>5} "
              f"{h['status']:<11} {LABEL_PRIORITAS[h['prioritas']]:<9} "
              f"{rupiah(h['nilai']):>14} {h['restock']:>8}")
    print("-" * lebar)

    total_item = len(hasil)
    total_nilai = sum(h["nilai"] for h in hasil)
    total_unit = sum(h["stok"] for h in hasil)
    termahal = max(hasil, key=lambda h: h["nilai"])
    perlu = sum(1 for h in hasil if h["status"] != "AMAN")

    print(f"Total nilai inventaris : {rupiah(total_nilai)}")
    print(f"Jumlah jenis barang    : {total_item}")
    print(f"Rata-rata stok/barang  : {total_unit / total_item:.1f} unit")
    print(f"Nilai stok terbesar    : {termahal['nama']} ({rupiah(termahal['nilai'])})")
    for status in ("HABIS", "RENDAH", "PERINGATAN", "AMAN"):
        jumlah = sum(1 for h in hasil if h["status"] == status)
        print(f"  {status:<11}: {jumlah:>2} item ({jumlah / total_item * 100:.1f}%)")
    print(f"Perlu restock          : {perlu} item ({perlu / total_item * 100:.1f}%)")
    print("=" * lebar)


def menu_peringatan_stok():
    print("\n--- CEK PERINGATAN STOK ---")
    cetak_laporan_stok(INVENTARIS)

    if baca_ya_tidak("\nTambah item baru ke inventaris? (y/n): "):
        nama = baca_teks("  Nama barang   : ")
        stok = baca_angka("  Stok          : ", int, 0, 100000)
        minimum = baca_angka("  Stok minimum  : ", int, 1, 100000)
        harga = baca_angka("  Harga satuan  : ", int, 1, 1_000_000_000)
        INVENTARIS.append({"nama": nama, "stok": stok,
                           "stok_minimum": minimum, "harga": harga})
        print("\nItem ditambahkan. Laporan terbaru:")
        cetak_laporan_stok(INVENTARIS)


# =====================================================================
# Menu utama
# =====================================================================

def tampilkan_menu():
    print("\n" + "=" * 40)
    print("SISTEM INFORMASI MAHASISWA".center(40))
    print("=" * 40)
    print("  1. Cek Status Mahasiswa")
    print("  2. Hitung Diskon Biaya")
    print("  3. Cek Peringatan Stok")
    print("  0. Keluar")
    print("-" * 40)


def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (0-3): ").strip()

        if pilihan == "1":
            menu_status_mahasiswa()
        elif pilihan == "2":
            menu_diskon_biaya()
        elif pilihan == "3":
            menu_peringatan_stok()
        elif pilihan == "0":
            print("\nTerima kasih. Program selesai.")
            break
        else:
            print("  Pilihan tidak valid. Masukkan angka 0 sampai 3.")


if __name__ == "__main__":
    main()