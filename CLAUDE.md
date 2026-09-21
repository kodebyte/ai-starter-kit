# Konvensi Project — Customer Support Assistant

## Stack
- Python 3.11+, FastAPI, SQLite (lewat SQLAlchemy)
- Semua response API wajib pakai Pydantic model — jangan return dict mentah
- Type hints wajib di semua function signature

## Struktur folder yang diharapkan
```
app/
├── main.py
├── routers/
├── models/
└── services/
```

## Gaya kode
- Nama endpoint & variabel dalam bahasa Inggris, komentar boleh bahasa Indonesia
- Error handling eksplisit — jangan biarkan exception mentah bocor ke response API
- Setiap fungsi service (bukan router) harus bisa di-test tanpa menjalankan server

## Data
- `data/products.json` dan `data/orders.csv` adalah mock data read-only untuk lab — jangan diubah strukturnya tanpa diskusi
- Baca data ini di layer `services/`, jangan langsung di router

## Kalau instruksi ambigu
Tanya dulu, jangan asumsi sendiri — terutama soal: nama field response, format error,
atau perilaku saat data tidak ditemukan (404 vs null vs error object).
