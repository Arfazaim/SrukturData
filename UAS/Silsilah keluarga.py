class Keluarga:
    def __init__(self, nama, gender, status, partner=None):
        self.nama = nama
        self.gender = gender
        self.status = status
        self.partner = partner
        self.anak = []

    def ortu(self, anak):
        self.ortu.append(ortu)

    def cari_nama(self, nama):
        if self.nama == nama:
            return self
        for anak in self.anak:
            result = anak.cari_nama(nama)
            if result:
                return result
        return None

    def print_keluarga(self, indent=0):
        print(" "*indent + self.nama + " (" + self.gender + ") - " + self.status, end="")
        if self.partner:
            print(" ♥ " + self.partner.nama)
        else:
            print()
        for anak in self.anak:
            anak.print_keluarga(indent+4)

keluarga_aku = Keluarga("Arfa Zaim", "L", "M")
keluarga_bapak = Keluarga("Khumaidi", "L", "K")
keluarga_ibu = Keluarga("Yusnaini", "P", "K")

keluarga_aku.ortu(keluarga_bapak)
keluarga_root.tambah_anak(keluarga_anak2)
keluarga_root.tambah_anak(keluarga_anak3)

keluarga_anak.partner = Keluarga("Winda", "P", "K")
keluarga_anak2.partner = Keluarga("Zaki", "L", "K")

keluarga_aku.print_keluarga()