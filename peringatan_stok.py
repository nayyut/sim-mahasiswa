"""peringatan_stok.py
Evaluasi status stok inventaris, laporan prioritas, total nilai inventaris,
dan ringkasan statistik.

Status stok (dibandingkan dengan stok minimum):
  - HABIS      : stok = 0                      -> prioritas 1 (Kritis)
  - RENDAH     : stok <= 50% stok minimum      -> prioritas 2 (Tinggi)
  - PERINGATAN : stok <= stok minimum          -> prioritas 3 (Sedang)
  - AMAN       : stok > stok minimum           -> prioritas 4 (-)
"""

INVENTARIS = [
    {"nama": "Kertas A4 (rim)",    "stok": 120, "stok_minimum": 50, "harga": 55000},
    {"nama": "Tinta Printer",      "stok": 18,  "stok_minimum": 20, "harga": 95000},
    {"nama": "Spidol Whiteboard",  "stok": 8,   "stok_minimum": 30, "harga": 12000},
    {"nama": "Map Folder",         "stok": 0,   "stok_minimum": 40, "harga": 3500},
    {"nama": "Baterai AA",         "stok": 45,  "stok_minimum": 40, "harga": 8000},
    {"nama": "Lakban",             "stok": 20,  "stok_minimum": 25, "harga": 9000},
    {"nama": "Penghapus Papan",    "stok": 0,   "stok_minimum": 15, "harga": 15000},
    {"nama": "Stapler",            "stok": 35,  "stok_minimum": 10, "harga": 28000},
    {"nama": "Flashdisk 32GB",     "stok": 6,   "stok_minimum": 15, "harga": 70000},
    {"nama": "Kabel HDMI",         "stok": 14,  "stok_minimum": 20, "harga": 45000},
]

LABEL_PRIORITAS = {1: "Kritis", 2: "Tinggi", 3: "Sedang", 4: "-"}


def rupiah(angka):
    return "Rp" + f"{angka:,.0f}".replace(",", ".")


def evaluasi_item(item):
    """Mengembalikan (status, prioritas)."""
    stok, minimum = item["stok"], item["stok_minimum"]
    if stok == 0:
        return "HABIS", 1
    if stok <= minimum * 0.5:
        return "RENDAH", 2
    if stok <= minimum:
        return "PERINGATAN", 3
    return "AMAN", 4


def analisis_inventaris(inventaris):
    """Menambahkan status, prioritas, nilai, dan saran restock ke tiap item."""
    hasil = []
    for item in inventaris:
        status, prioritas = evaluasi_item(item)
        perlu = status != "AMAN"
        hasil.append({
            **item,
            "status": status,
            "prioritas": prioritas,
            "nilai": item["stok"] * item["harga"],
            # target restock = 2x stok minimum
            "restock": max(0, item["stok_minimum"] * 2 - item["stok"]) if perlu else 0,
        })
    hasil.sort(key=lambda x: (x["prioritas"], x["nama"]))
    return hasil


def cetak_laporan_stok(inventaris):
    hasil = analisis_inventaris(inventaris)
    lebar = 98

    print("\n" + "=" * lebar)
    print("LAPORAN PERINGATAN STOK".center(lebar))
    print("=" * lebar)
    print(f"{'No':<3} {'Nama Barang':<20} {'Stok':>5} {'Min':>5} {'Status':<11} "
          f"{'Prioritas':<9} {'Nilai Stok':>14} {'Restock':>8}")
    print("-" * lebar)
    for no, h in enumerate(hasil, start=1):
        print(f"{no:<3} {h['nama']:<20} {h['stok']:>5} {h['stok_minimum']:>5} "
              f"{h['status']:<11} {LABEL_PRIORITAS[h['prioritas']]:<9} "
              f"{rupiah(h['nilai']):>14} {h['restock']:>8}")
    print("-" * lebar)

    # ---- Statistik ----
    total_item = len(hasil)
    if total_item == 0:
        print("Inventaris kosong.")
        return

    total_nilai = sum(h["nilai"] for h in hasil)
    total_unit = sum(h["stok"] for h in hasil)
    termahal = max(hasil, key=lambda h: h["nilai"])
    total_restock = sum(h["restock"] for h in hasil)
    biaya_restock = sum(h["restock"] * h["harga"] for h in hasil)

    print(f"Total nilai inventaris : {rupiah(total_nilai)}")
    print("\nRINGKASAN STATISTIK")
    print(f"  Jumlah jenis barang        : {total_item}")
    print(f"  Total unit di gudang       : {total_unit}")
    print(f"  Rata-rata stok per barang  : {total_unit / total_item:.1f} unit")
    print(f"  Rata-rata nilai per barang : {rupiah(total_nilai / total_item)}")
    print(f"  Nilai stok terbesar        : {termahal['nama']} "
          f"({rupiah(termahal['nilai'])})")
    print("  Sebaran status:")
    for status in ("HABIS", "RENDAH", "PERINGATAN", "AMAN"):
        jumlah = sum(1 for h in hasil if h["status"] == status)
        print(f"    {status:<11}: {jumlah:>2} item ({jumlah / total_item * 100:.1f}%)")
    perlu_restock = sum(1 for h in hasil if h["status"] != "AMAN")
    print(f"  Perlu restock              : {perlu_restock} item "
          f"({perlu_restock / total_item * 100:.1f}%)")
    print(f"  Saran restock total        : {total_restock} unit "
          f"(perkiraan biaya {rupiah(biaya_restock)})")
    print("=" * lebar)


def main():
    cetak_laporan_stok(INVENTARIS)


if __name__ == "__main__":
    main()