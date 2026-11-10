import os
import subprocess
import time
from PIL import Image, ImageEnhance

project_dir = r"C:\Users\Administrator\Documents\Project\pmb umnu"
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
revisi_dir = os.path.join(project_dir, "2_REVISI_UIUX_SETELAH_PERBAIKAN")
wf_dir = os.path.join(project_dir, "WIREFRAME_HITAM_PUTIH")

# 1. Update High-Fidelity Screenshots in 2_REVISI_UIUX_SETELAH_PERBAIKAN
pages_to_update = [
    ("program-studi.html", "03_Program_Studi.png", 1200, 2400),
    ("program-studi-detail-55202.html", "04_Detail_Prodi_TI.png", 1200, 3200),
]

for html_file, png_name, w, h in pages_to_update:
    out_path = os.path.join(revisi_dir, png_name)
    url = f"http://localhost:8080/{html_file}"
    cmd = [
        chrome_path,
        "--headless",
        "--no-sandbox",
        "--disable-gpu",
        f"--window-size={w},{h}",
        f"--screenshot={out_path}",
        url
    ]
    print(f"Updating High-Fi screenshot: {png_name}...")
    subprocess.run(cmd, check=True)
    time.sleep(1)

# Also copy to HALAMAN_UNTUK_FIGMA
figma_dir = os.path.join(project_dir, "HALAMAN_UNTUK_FIGMA", "2_REVISI_UIUX_SETELAH_PERBAIKAN")
if os.path.exists(figma_dir):
    import shutil
    shutil.copy(os.path.join(revisi_dir, "03_Program_Studi.png"), os.path.join(figma_dir, "03_Program_Studi.png"))
    shutil.copy(os.path.join(revisi_dir, "04_Detail_Prodi_TI.png"), os.path.join(figma_dir, "04_Detail_Prodi_TI.png"))

# 2. Re-run generate_all_wireframes.py to update WIREFRAME_HITAM_PUTIH
print("\nRe-generating WIREFRAME_HITAM_PUTIH...")
subprocess.run(["python", "generate_all_wireframes.py"], check=True)

print("\nALL UPDATED SUCCESSFULLY WITH THE 5 EVALUATION POINTS!")
