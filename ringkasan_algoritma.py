# ---------------------------------------------------------------------
# Data contoh
# ---------------------------------------------------------------------

# (nim, nama, ipk, sks)
MAHASISWA = [
    ("2022101001", "Andi Pratama",  3.65, 22),
    ("2022101002", "Bunga Lestari", 2.10, 20),
    ("2023101003", "Candra Wijaya", 1.80, 18),
    ("2023101004", "Dewi Anggraini", 3.20, 24),
    ("2023101005", "Eko Saputra",   1.20, 12),
    ("2024101006", "Fitri Handayani", 2.75, 15),
    ("2024101007", "Gilang Ramadhan", 1.45, 10),
    ("2024101008", "Hana Permata",  3.90, 21),
    ("2021101009", "Irfan Maulana", 2.00, 18),
    ("2021101010", "Jihan Aulia",   0.95, 6),
]

# (spp, anak_karyawan, ipk, tepat_waktu)
TRANSAKSI_DISKON = [
    (5_000_000, True,  3.90, True),
    (5_000_000, False, 3.60, True),
    (4_500_000, False, 3.10, False),
    (4_500_000, True,  2.80, False),
    (6_000_000, False, 2.50, True),
    (6_000_000, False, 3.85, False),
    (5_500_000, True,  3.55, True),
    (5_500_000, False, 2.20, False),
]

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


# ---------------------------------------------------------------------
# Algoritma studi kasus (sama dengan program sebelumnya)
# ---------------------------------------------------------------------

def tentukan_status(ipk, sks):
    if ipk < 1.5:
        return "Tidak Aktif"
    if ipk >= 2.0 and sks >= 18:
        return "Aktif"
    return "Peringatan"


def persen_diskon(anak_karyawan, ipk, tepat_waktu):
    total = 25 if anak_karyawan else 0
    if ipk >= 3.8:
        total += 20
    elif ipk >= 3.5:
        total += 15
    elif ipk >= 3.0:
        total += 10
    if tepat_waktu:
        total += 5
    return total


def perlu_restock(item):
    return item["stok"] <= item["stok_minimum"]


def rupiah(angka):
    return "Rp" + f"{angka:,.0f}".replace(",", ".")


# ---------------------------------------------------------------------
# Perhitungan ringkasan
# ---------------------------------------------------------------------

def ringkas_mahasiswa():
    status = [tentukan_status(ipk, sks) for _, _, ipk, sks in MAHASISWA]
    total = len(status)
    return [
        ("Total mahasiswa", str(total), "100.0%"),
        ("Aktif", str(status.count("Aktif")),
         f"{status.count('Aktif') / total * 100:.1f}%"),
        ("Peringatan", str(status.count("Peringatan")),
         f"{status.count('Peringatan') / total * 100:.1f}%"),
        ("Tidak Aktif", str(status.count("Tidak Aktif")),
         f"{status.count('Tidak Aktif') / total * 100:.1f}%"),
    ]


def ringkas_diskon():
    persen = [persen_diskon(k, i, t) for _, k, i, t in TRANSAKSI_DISKON]
    potongan = [spp * p / 100 for (spp, *_), p in zip(TRANSAKSI_DISKON, persen)]
    n = len(persen)
    return [
        ("Jumlah transaksi", str(n), "-"),
        ("Rata-rata diskon", f"{sum(persen) / n:.1f}%", "-"),
        ("Diskon tertinggi / terendah", f"{max(persen)}% / {min(persen)}%", "-"),
        ("Rata-rata potongan", rupiah(sum(potongan) / n), "-"),
    ]


def ringkas_stok():
    total = len(INVENTARIS)
    restock = sum(1 for item in INVENTARIS if perlu_restock(item))
    return [
        ("Total item", str(total), "100.0%"),
        ("Perlu restock", str(restock), f"{restock / total * 100:.1f}%"),
        ("Stok aman", str(total - restock), f"{(total - restock) / total * 100:.1f}%"),
    ]


# ---------------------------------------------------------------------
# Tampilan tabel
# ---------------------------------------------------------------------

def cetak_tabel(judul_kolom, baris, lebar):
    garis = "+" + "+".join("-" * (w + 2) for w in lebar) + "+"

    def format_baris(isi):
        sel = []
        for i, (teks, w) in enumerate(zip(isi, lebar)):
            sel.append(f" {teks:<{w}} " if i == 0 else f" {teks:>{w}} ")
        return "|" + "|".join(sel) + "|"

    print(garis)
    print(format_baris(judul_kolom))
    print(garis)
    for b in baris:
        print(format_baris(b))
    print(garis)


def main():
    lebar = [30, 16, 10]
    kolom = ("Metrik", "Nilai", "Persentase")

    print("\nRINGKASAN ALGORITMA SISTEM INFORMASI MAHASISWA")

    print("\n(a) Status Mahasiswa: Aktif vs Tidak Aktif")
    cetak_tabel(kolom, ringkas_mahasiswa(), lebar)

    print("\n(b) Diskon Biaya Kuliah")
    cetak_tabel(kolom, ringkas_diskon(), lebar)

    print("\n(c) Peringatan Stok")
    cetak_tabel(kolom, ringkas_stok(), lebar)


if __name__ == "__main__":
    main()