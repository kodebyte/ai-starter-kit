# Customer Support Assistant — Starter Kit

Starter-kit untuk training AI 3 hari: Agentic Workflows (Hari 1) → RAG (Hari 2) → Security (Hari 3).

Folder `app/` sengaja **kosong**. Ini bukan bug — Sesi 1 memang mengajarkan kamu men-scaffold
project ini dari nol pakai Claude Code (vibe coding), bukan pakai kode yang sudah jadi.

## Isi starter-kit

| Folder/File | Isi |
| --- | --- |
| `data/products.json` | Mock data produk (nama, stok, harga) |
| `data/orders.csv` | Mock data order pelanggan (dipakai lintas 3 hari) |
| `docs/` | Kosong — diisi FAQ/manual produk di Hari 2 |
| `app/` | Kosong — kamu yang scaffold pakai Claude Code |
| `CLAUDE.md` | Konvensi kode yang dibaca otomatis oleh Claude Code |
| `.env.example` | Template API key (Anthropic + Gemini fallback) |

## Setup awal

```bash
cp .env.example .env
# isi ANTHROPIC_API_KEY dan GEMINI_API_KEY di .env
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Starter prompts (coba ini di Claude Code)

Jalankan `claude` di root folder ini, lalu coba prompt berikut secara berurutan:

**1. Scaffolding**
```
Baca data/products.json dan data/orders.csv, lalu scaffold FastAPI app di folder app/
dengan struktur routers/, models/, services/. Buat endpoint:
- GET /stock/{product_name} -> cek stok produk
- GET /orders/{order_id} -> cek detail & status order
Gunakan Pydantic model untuk semua response.
```

**2. Debugging** (setelah instruktur menyisipkan 1 bug)
```
Endpoint GET /orders/{order_id} melempar error ini: [paste error trace]
Jelaskan dulu root cause-nya sebelum kasih fix.
```

**3. Auto unit test**
```
Generate unit test untuk endpoint GET /orders/{order_id}.
Cover case: order ditemukan, order tidak ditemukan, order_id format invalid.
```

**4. Context engineering** (bandingkan hasilnya)
```
Tanpa menyebut file spesifik: "Tambahkan validasi kalau stok produk negatif"
vs
Dengan context eksplisit: "Di @app/models/product.py, tambahkan validasi kalau stok produk negatif"
```

## Kalau stuck

Checkout checkpoint solusi Sesi 1 (jangan dipakai sebelum benar-benar coba sendiri):

```bash
git checkout checkpoint/sesi1-done
```
