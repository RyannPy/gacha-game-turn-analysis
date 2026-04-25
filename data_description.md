# Dataset Description

## Data Generation

Data ini merupakan data sintetis yang dibuat untuk mensimulasikan perilaku pemain game gacha.

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
