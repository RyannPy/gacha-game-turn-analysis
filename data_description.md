# Dataset Description

## Data Generation

Data ini merupakan data sintetis yang dibuat untuk mensimulasikan perilaku pemain game gacha. Berikut proses lengkap dan logic dibalik data generation:

- churn_score :
  Meningkat berdasarkan beberapa variabel lain. Ini jadi salah satu komponen yang menentukan tingkat churn player.

- Hardware :
  Menentukan hardware secara acak, dengan base_fps tergantung dari hardware player. Fps akan turun seiring minggu dengan decay_rate, menghasilkam avg_fps_week dalam 8 minggu.

- Gacha / Spin / Pull :
  Dengan soft_pity di angka 80, kita bisa menentukan bahwa total_pulls per ssr_obtained akan menambah churn_score apabila melebihi nilai soft_pity. Hal ini diperkuat jika got_target_character tidak didapatkan oleh player.

- Story Progress :
  Progress cerita mempengaruhi churn_score apabila ssr_obtained masih sedikit, dikarenakan tempat untuk mendapatkan kurensi pull tersisa sedikit sedangkan ssr_obtained masih sedikit.

- Session Time :
  Waktu sesi bermain akan dipengaruhi oleh churn_effect dan hardware. Semakin tinggi dampak dari churn_score dan fps_effect, semakin besar kemungkinan player berhenti (churn).

## Struktur Data

Setiap baris merepresentasikan:

> 1 pemain dalam 1 minggu (time-series data)

## Kolom

- user_id
  Id unik user

- week
  Minggu ke-n aktivitas pemain

- session_time
  Total waktu bermain (jam) dalam 1 minggu

- device_class
  Kategori device (low, medium, high)

- avg_fps
  Rata-rata FPS selama bermain

- total_pulls
  Total jumlah gacha yang dilakukan

- ssr_obtained
  Jumlah karakter rarity tinggi yang didapat

- got_target
  Apakah pemain mendapatkan karakter target (1 = ya, 0 = tidak)

- story_progress
  Progress cerita (0–100%)

- churn
  Status churn (1 = berhenti, 0 = masih aktif)

## Asumsi Data

- FPS rendah menurunkan kenyamanan bermain
- Hasil gacha buruk meningkatkan kemungkinan churn
- Aktivitas bermain yang menurun mengindikasikan potensi churn
- Pemain endgame tanpa progres cenderung berhenti

## Catatan

Dataset ini bukan data nyata, melainkan simulasi untuk tujuan pembelajaran.
