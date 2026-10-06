def rupiah(angka):
    return "Rp" + f"{angka:,.0f}".replace(",", ".")


def baca_spp(prompt):
    while True:
        teks = input(prompt).strip().replace(".", "").replace(",", ".")
        try:
            nilai = float(teks)
        except ValueError:
            print("  Masukkan angka saja, contoh: 5000000")
            continue
        if nilai > 0:
            return nilai
        print("  Biaya SPP harus lebih dari 0.")


def baca_ipk(prompt):
    while True:
        teks = input(prompt).strip().replace(",", ".")
        try:
            nilai = float(teks)
        except ValueError:
            print("  IPK harus berupa angka.")
            continue
        if 0.0 <= nilai <= 4.0:
            return nilai
        print("  IPK harus antara 0.0 dan 4.0.")


def baca_ya_tidak(prompt):
    while True:
        jawab = input(prompt).strip().lower()
        if jawab in ("y", "n"):
            return jawab == "y"
        print("  Jawab dengan 'y' atau 'n'.")


def hitung_diskon(spp, anak_karyawan, ipk, tepat_waktu):
    """Mengembalikan (daftar_rincian, total_persen, potongan, biaya_final)."""
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


def cetak_hasil(spp, rincian, total_persen, potongan, final):
    print("\n" + "=" * 46)
    print("RINCIAN DISKON BIAYA KULIAH".center(46))
    print("=" * 46)
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


def main():
    print("=== Kalkulator Diskon Biaya Kuliah ===")
    spp = baca_spp("Biaya SPP (Rp)                : ")
    anak_karyawan = baca_ya_tidak("Anak karyawan? (y/n)          : ")
    ipk = baca_ipk("IPK (0.0 - 4.0)               : ")
    tepat_waktu = baca_ya_tidak("Bayar tepat waktu? (y/n)      : ")

    hasil = hitung_diskon(spp, anak_karyawan, ipk, tepat_waktu)
    cetak_hasil(spp, *hasil)


if __name__ == "__main__":
    main()