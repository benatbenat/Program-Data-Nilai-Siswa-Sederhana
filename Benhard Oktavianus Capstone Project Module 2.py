from prettytable import PrettyTable

# Format : NIS, Nama, Kelas, Jurusan, Mata pelajaran, Nilai, Status(Nilai)

data_siswa = [
    [102341, "Andi", "10A", "IPA", "Matematika", 85, "Lulus"],
    [102342, "Budi", "10B", "IPS", "Sejarah", 78, "Lulus"],
    [102343, "Citra", "11A", "IPA", "Fisika", 92, "Lulus"],
    [102344, "Dewi", "11B", "IPS", "Geografi", 65, "Remedial"],
    [102345, "Eka", "12A", "IPA", "Kimia", 88, "Lulus"],
]

data_recycle = []

# Fungsi Helper

def cari_index_siswa(nis):
    # Mencari index siswa dalam list berdasarkan NIS. Return -1 jika tidak ada.
    for i in range(len(data_siswa)):
        # data_siswa[i][0] adalah NIS
        if data_siswa[i][0] == nis:
            return i
    return -1

def generate_nis_baru():
    # Mencari NIS terbesar di list dan menambah 1
    if len(data_siswa) == 0:
        return 102341
    
    max_nis = 0
    for siswa in data_siswa:
        if siswa[0] > max_nis:
            max_nis = siswa[0]
    return max_nis + 1

def hitung_status(nilai):
    return "Lulus" if nilai >= 75 else "Remedial"

def validasi_input_nilai(pesan, nilai_lama=None):
    # Looping sampai user memasukkan angka 0-100 yang valid
    while True:
        isi = input(pesan)
        
        # Jika kosong dan ada nilai lama (mode update), pakai nilai lama
        if isi == "" and nilai_lama is not None:
            return nilai_lama
        
        try:
            angka = int(isi)
            if 0 <= angka <= 100:
                return angka
            else:
                print(">> Error: Nilai harus 0-100.")
        except ValueError:
            print(">> Error: Masukkan angka bulat.")

def tampilkan_tabel(data_source, judul):
    if len(data_source) == 0:
        print(f"\n>> {judul} Kosong.")
        return

    tabel = PrettyTable()
    tabel.field_names = ["No", "NIS", "Nama", "Kelas", "Jurusan", "Mata Pelajaran", "Nilai", "Status"]
    
    # Menggunakan enumerate untuk nomor urut
    for i, row in enumerate(data_source):
        # Membentuk row baru dengan nomor urut di depan
        row_lengkap = [i + 1] + row 
        tabel.add_row(row_lengkap)
    
    print(f"\n-+-+- {judul} -+-+-")
    print(tabel)

# Fungsi Menu Utama

def menu_tambah():
    print("\n[ TAMBAH DATA SISWA ]")
    nama = input("Nama            : ")
    kelas = input("Kelas           : ")
    jurusan = input("Jurusan         : ")
    mapel = input("Mata Pelajaran  : ")
    nilai = validasi_input_nilai("Nilai (0-100)   : ")
    
    
    nis = generate_nis_baru()
    status = hitung_status(nilai)
    
    # Masukkan ke list utama
    data_baru = [nis, nama, kelas, jurusan, mapel, nilai, status]
    data_siswa.append(data_baru)
    print(f">> Sukses! Siswa {nama} ditambahkan dengan NIS {nis}.")
    tampilkan_tabel(data_siswa, "Daftar Nilai Siswa")

def menu_update():
    while True:
        print("\n[ UPDATE DATA ]")
        print("1. Update Semua Kolom")
        print("2. Update Nilai Saja")
        print("3. Kembali")
        
        pilih = input("Pilih (1-3): ")
        if pilih == '3':
            break
        
        if pilih not in ['1', '2']:
            print(">> Pilihan salah.")
            continue
            
        tampilkan_tabel(data_siswa, "Data Saat Ini")
        
        try:
            nis_input = input('''Note : Kosongkan jika data tidak ingin diubah 
            Masukkan NIS yang akan diupdate (Enter untuk kembali):''')
            if nis_input == "": continue
            nis = int(nis_input)
        except ValueError:
            print(">> NIS harus angka.")
            continue
            
        idx = cari_index_siswa(nis)
        
        if idx == -1:
            print(f">> NIS {nis} tidak ditemukan.")
        else:
            # Ambil referensi list siswa yang mau diedit
            # Format: [NIS, Nama, Kelas, Jurusan, Mapel, Nilai, Status]
            siswa_lama = data_siswa[idx]
            print(f"Mengedit: {siswa_lama[1]}")
            
            if pilih == '1':
                # Update Semua (kecuali NIS)
                # Gunakan 'or' agar jika di-enter kosong, nilai tidak berubah
                nama_baru = input(f"Nama [{siswa_lama[1]}]: ") or siswa_lama[1]
                kelas_baru = input(f"Kelas [{siswa_lama[2]}]: ") or siswa_lama[2]
                jur_baru = input(f"Jurusan [{siswa_lama[3]}]: ") or siswa_lama[3]
                mapel_baru = input(f"Mapel [{siswa_lama[4]}]: ") or siswa_lama[4]
                nilai_baru = validasi_input_nilai(f"Nilai [{siswa_lama[5]}]: ", siswa_lama[5])
                status_baru = hitung_status(nilai_baru)
                
                # Timpa data di list utama
                data_siswa[idx] = [nis, nama_baru, kelas_baru, jur_baru, mapel_baru, nilai_baru, status_baru]
                print(">> Data berhasil diupdate lengkap.")
                tampilkan_tabel(data_siswa, "Data Setelah Update")
                
            elif pilih == '2':
                # Update Nilai Saja
                nilai_baru = validasi_input_nilai(f"Nilai Baru [{siswa_lama[5]}]: ", siswa_lama[5])
                status_baru = hitung_status(nilai_baru)
                
                # Update index ke-5 (Nilai) dan ke-6 (Status) secara langsung
                data_siswa[idx][5] = nilai_baru
                data_siswa[idx][6] = status_baru
                print(">> Nilai berhasil diupdate.")
                tampilkan_tabel(data_siswa, "Data Setelah Update")

def menu_hapus():
    while True:
        print("\n[ HAPUS DATA ]")
        tampilkan_tabel(data_siswa, "Daftar Siswa")
        
        try:
            nis_input = input("\nMasukkan NIS untuk dihapus (Enter untuk kembali): ")
            if nis_input == "": break
            nis = int(nis_input)
        except ValueError:
            print(">> Input harus angka.")
            continue
            
        idx = cari_index_siswa(nis)
        
        if idx == -1:
            print(">> Data tidak ditemukan.")
        else:
            # Hapus dari list utama dan simpan ke variabel
            siswa_terhapus = data_siswa.pop(idx)
            # Masukkan ke list recycle bin
            data_recycle.append(siswa_terhapus)
            print(f">> Siswa {siswa_terhapus[1]} dipindahkan ke Recycle Bin.")

def menu_recycle_bin():
    while True:
        print(f"\n[ RECYCLE BIN - {len(data_recycle)} Item ]")
        print("1. Lihat & Restore Data")
        print("2. Hapus Permanen Semuanya")
        print("3. Kembali")
        
        pilih = input("Pilih: ")
        
        if pilih == '3':
            break
            
        if pilih == '1':
            if len(data_recycle) == 0:
                print(">> Kosong.")
                continue
                
            tampilkan_tabel(data_recycle, "Isi Recycle Bin")
            
            try:
                nis_input = input("\nMasukkan NIS untuk di Restore (Enter batal): ")
                if nis_input == "": continue
                nis_restore = int(nis_input)
                
                # Mencari manual di list recycle
                index_ketemu = -1
                for i in range(len(data_recycle)):
                    if data_recycle[i][0] == nis_restore:
                        index_ketemu = i
                        break
                
                if index_ketemu != -1:
                    # Kembalikan ke data utama
                    siswa_pulih = data_recycle.pop(index_ketemu)
                    data_siswa.append(siswa_pulih)
                    
                    # Sort manual list utama berdasarkan NIS (Index 0)
                    # Menggunakan lambda untuk sort data berdasarkan NIS
                    data_siswa.sort(key=lambda x: x[0]) 
                    
                    print(f">> Data {siswa_pulih[1]} berhasil di Restore.")
                else:
                    print(">> NIS tidak ada di Recycle Bin.")
                    
            except ValueError:
                print(">> Error input.")
                
        elif pilih == '2':
            if len(data_recycle) > 0:
                yakin = input("Yakin hapus permanen? (y/n): ")
                if yakin.lower() == 'y':
                    data_recycle.clear() # Untuk menghapus bersih data
                    print(">> Recycle Bin kosong.")
            else:
                print(">> Sudah kosong.")

# Program Utama

while True:
    print("\n" + "+="*13)
    print(" PROGRAM DATA NILAI SISWA")
    print("+="*13)
    print("1. Tampilkan Data")
    print("2. Tambah Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("5. Recycle Bin")
    print("6. Keluar")
    print("-" * 26)
    
    menu = input("Pilih Menu (1-6): ")
    
    if menu == '1':
        tampilkan_tabel(data_siswa, "Daftar Nilai Siswa")
    elif menu == '2':
        menu_tambah()
    elif menu == '3':
        menu_update()
    elif menu == '4':
        menu_hapus()
    elif menu == '5':
        menu_recycle_bin()
    elif menu == '6':
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print(">> Pilihan tidak tersedia.")