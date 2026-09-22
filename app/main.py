from fastapi import FastAPI

app = FastAPI(title="Customer Support Assistant")


@app.get("/health")
def health_check():
    """Endpoint verifikasi awal -- dipakai sebelum Sesi 1 untuk cek setup sudah benar.
    Endpoint asli (stock, orders, chat) di-scaffold di Sesi 1 lewat vibe coding,
    menambah ke file ini, bukan menggantikannya dari nol."""
    return {"status": "ok"}
