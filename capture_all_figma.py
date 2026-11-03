import subprocess
import os
import time

pages = [
    ("http://localhost:8080/index.html", "01_Beranda_REVISI.png", 1200, 3200),
    ("http://localhost:8080/jalur-seleksi.html", "02_Jalur_Pendaftaran_REVISI.png", 1200, 2400),
    ("http://localhost:8080/program-studi.html", "03_Program_Studi_REVISI.png", 1200, 2400),
    ("http://localhost:8080/program-studi-detail-55202.html", "04_Detail_Prodi_TI_REVISI.png", 1200, 2400),
    ("http://localhost:8080/pengumuman.html", "05_Informasi_Pengumuman_REVISI.png", 1200, 2400),
    ("http://localhost:8080/detail-pengumuman-10.html", "06_Detail_Pengumuman_REVISI.png", 1200, 2400),
    ("http://localhost:8080/login.html", "07_Login_Masuk_REVISI.png", 1200, 2400),
    ("http://localhost:8080/user-guide.html", "08_Petunjuk_Pendaftaran_REVISI.png", 1200, 2400),
]

output_dir = os.path.abspath("HALAMAN_UNTUK_FIGMA")
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

for url, filename, w, h in pages:
    out_path = os.path.join(output_dir, filename)
    cmd = [
        chrome_path,
        "--headless",
        "--no-sandbox",
        "--disable-gpu",
        f"--window-size={w},{h}",
        f"--screenshot={out_path}",
        url
    ]
    print(f"Capturing {filename}...")
    subprocess.run(cmd, check=True)
    time.sleep(1)

print("\nAll 8 updated page screenshots captured successfully in HALAMAN_UNTUK_FIGMA!")
