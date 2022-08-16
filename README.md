<div id="deskripsi">
  <hr>
  <h3>Deskripsi Singkat Project</h3>
  Pada project ini, akan dilakukan identifikasi nilai mata uang rupiah dengan menggabungkan metode ekstrasi ciri 
  Local Binary Pattern dan metode klasifikasi Naïve Bayes. Serta untuk pengukuran akurasi identifikasi dilakukan dengan metode evaluasi K-Fold Cross Validation. 
  Dataset yang digunakan berupa citra dengan rincian terdapat 120 citra yang terdiri dari 15 citra uang kertas Rp1.000, 15 citra uang kertas Rp2.000, 15 citra uang kertas Rp5.000, 15 citra uang kertas Rp10.000, 15 citra uang kertas Rp20.000, 15 citra uang kertas Rp50.000, 15 citra uang kertas Rp75.000, dan 15 citra uang kertas Rp100.000
</div>

<div id="tahapan">
  <hr>
  <h3>Tahapan Identifikasi</h3>
  <ul>
  <li>
    Akuisisi Data <br>
    Bagian akuisisi data digunakan untuk memperoleh data latih serta data uji untuk penelitian. Dalam 
    pengambilannya, peneliti mengambil gambar uang yang difoto di atas kertas HVS. <br>
    Contoh : <br>
    <img width="50%" alt="image" src="https://user-images.githubusercontent.com/96558726/184837924-1ef0b3fc-b774-47da-ab13-7ec399e42fd3.jpg"> <br>
  </li>
  <li>
    Konversi Grayscale <br>
    <img width="50%" alt="image" src="https://user-images.githubusercontent.com/96558726/184836354-4a7a5b5a-8d4c-42d8-9cc7-e0c3cbe4c6cf.png"> <br>
    Pada bagian ini, citra dikonversi kedalam mode grayscale yang bertujuan untuk memenuhi syarat citra agar dapat
    dilakukan ekstrasi ciri.
  </li>
  <li>
    Ekstrasi Ciri <br>
    Metode ekstrasi ciri yang digunakan pada penelitian ini adalah Local Binary Pattern (LBP). Terdapat beberapa 
    tahapan dalam penggunaan LBP, yaitu sebagai berikut. <br>
    1. Lakukan inisialisasi terhadap (x, y) dan varibel nilai yang berguna sebagai penampung nilai yang nantinya 
    menggantikan nilai piksel tengah. <br>
    2. Menggunakan kondisi x > 0 dan x < lebar citra dikurang 1 dan y > 0 dan y < tinggi citra dikurang 1.
    3. Apabila kondisi tersebut terpenuhi maka ambil nilai piksel tengah ic dan piksel ketetanggaan dari i7 
    sampai i0. <br>
    4. Lakukan perbandingan nilai piksel tengah ic dengan piksel ketetanggaan, apabila nilai ic >= piksel 
    ketetanggaan maka dilakukan penjumlahan pada variabel nilai sesuai dengan bobot masing-masing piksel 
    ketetanggaan. <br>
    5. Ubah semua nilai warna pada piksel (x,y) dengan value pada variabel nilai. <br>
    6. Lakukan penjumlahan nilai y dan memproses piksel selanjutnya. Setelah semua piksel diproses maka 
    akan terbentuk citra hasil LBP. <br>
  </li>
  <li>
    Klasifikasi <br>
    Metode klasifikasi yang digunakan pada penelitian ini adalah Naïve Bayes. Terdapat beberapa tahapan dalam 
    penggunaan Naïve Bayes, yaitu sebagai berikut. <br>
    1. Mencari probabilitas setiap atribut terhadap kelas <br>
    2. Menetapkan data sampel yang inigin diuji kelasnya ke dalam variabel, misal X <br>
    3. Menetapkan hipotests bahwa X adalah data dengan kelas label tertentu kedalma variabel, misal Y <br>
    4. Cari prior yaitu peluang dari hipotesis Y <br>
    5. Cari evidence yaitu peluang data sampel yang diamati <br>
    6. Cari likelihood yaitu peluang data sampel X, bila diasumsikan bahwa hipotesis Y benar <br>
    7. Untuk klasifikasi, cari posterior dengan nilai terbesar yang didapat dari perhitumgan likelihood dikali 
    prior dibagi evidence <br>
  </li>
  <li>
    Evaluasi <br>
    Setelah citra diekstrasi dan diklasifikasi, maka pada tahap ini dilakukan perhitungan akurasi pengujian 
    menggunakan K-Fold Cross Validation.
  </li>
  </ul>
</div>

<div id="tampilan">
  <hr>
  <h3>Screenshoot tampilan GUI aplikasi</h3>
  Halaman menu home <br>
  <img width="400" alt="image" src="https://user-images.githubusercontent.com/96558726/184838647-2952a804-46db-4d01-831f-a705500bff05.png"> <br>
  Input directory image yang ingin di klasifikasi <br>
  <img width="395" alt="image" src="https://user-images.githubusercontent.com/96558726/184838800-0ef2c0c1-8c61-41cc-8d5b-b80f75ee2308.png"><br>
  Hasil kalsifikasi <br>
  <img width="398" alt="image" src="https://user-images.githubusercontent.com/96558726/184838886-2723d9ea-379a-479e-9b0f-ba185d24d84e.png"><br>
  Halaman menu dataset <br>
  <img width="400" alt="image" src="https://user-images.githubusercontent.com/96558726/184839009-9f59a895-c6e3-4246-9d42-4e86ca03d640.png"><br>
  Halaman menu plot <br>
  <img width="404" alt="image" src="https://user-images.githubusercontent.com/96558726/184839121-1a7b9082-13b2-4505-9f47-f2a405505e03.png"><br>
</div>
