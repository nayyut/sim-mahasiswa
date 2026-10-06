from src.models import Mahasiswa, DaftarMahasiswa


def test_tambah_mahasiswa():
    db = DaftarMahasiswa()

    mhs = Mahasiswa(
        nim="123456",
        nama="Nayla",
        program_studi="Sistem Informasi",
        angkatan=2026,
        ipk=3.75
    )

    db.tambah(mhs)

    assert db.jumlah == 1
    assert db.cari("123456") == mhs


def test_cari_mahasiswa():
    db = DaftarMahasiswa()

    mhs = Mahasiswa(
        nim="123456",
        nama="Nayla",
        program_studi="Sistem Informasi",
        angkatan=2026,
        ipk=3.75
    )

    db.tambah(mhs)

    hasil = db.cari("123456")

    assert hasil is not None
    assert hasil.nama == "Nayla"


def test_hapus_mahasiswa():
    db = DaftarMahasiswa()

    mhs = Mahasiswa(
        nim="123456",
        nama="Nayla",
        program_studi="Sistem Informasi",
        angkatan=2026,
        ipk=3.75
    )

    db.tambah(mhs)

    berhasil = db.hapus("123456")

    assert berhasil is True
    assert db.jumlah == 0