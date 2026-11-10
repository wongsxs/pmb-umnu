import os
import re
import subprocess
import time
from PIL import Image, ImageEnhance

project_dir = r"C:\Users\Administrator\Documents\Project\pmb umnu"
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
out_dir = os.path.join(project_dir, "WIREFRAME_HITAM_PUTIH")
os.makedirs(out_dir, exist_ok=True)

wireframe_css = """
<link href="https://fonts.googleapis.com/css2?family=Material+Icons+Round&display=swap" rel="stylesheet" />
<style id="wireframe-theme">
    /* ==========================================================================
       AUTHENTIC LOW-FIDELITY WIREFRAME THEME (BLACK & WHITE / GRAYSCALE)
       ========================================================================== */
    * {
        box-shadow: none !important;
        text-shadow: none !important;
    }

    body, html {
        background-color: #ffffff !important;
        background-image: radial-gradient(#cbd5e1 1.2px, transparent 1.2px) !important;
        background-size: 22px 22px !important;
        color: #0f172a !important;
        font-family: 'Inter', system-ui, -apple-system, sans-serif !important;
    }

    /* 1. Header */
    .navbar__landingpage {
        background: #ffffff !important;
        border-bottom: 2px solid #0f172a !important;
        box-shadow: none !important;
    }
    .navbar__landingpage .navbar-info .info-kampus-logo img,
    .info-kampus-logo img {
        filter: grayscale(100%) contrast(150%) !important;
        border: 2px solid #0f172a !important;
        border-radius: 50% !important;
        background: #e2e8f0 !important;
    }
    .navbar__landingpage .navbar-info .info-kampus-text h1 {
        color: #0f172a !important;
    }
    .navbar__landingpage .navbar-info .info-kampus-text p {
        color: #64748b !important;
    }
    .navbar__landingpage .navbar-menu li a.navbar-item {
        color: #334155 !important;
        font-weight: 600 !important;
    }
    .navbar__landingpage .navbar-menu li.active a.navbar-item {
        color: #000000 !important;
        background: #e2e8f0 !important;
        border: 1.5px solid #0f172a !important;
        border-radius: 6px !important;
    }
    .cta-language {
        background: #ffffff !important;
        border: 1.5px solid #0f172a !important;
        color: #0f172a !important;
        border-radius: 6px !important;
    }

    /* 2. Hero Banner */
    #banner-section {
        background: #f1f5f9 !important;
        background-image: none !important;
        border: 2px dashed #64748b !important;
        border-radius: 14px !important;
        margin: 25px auto !important;
        padding: 45px 35px !important;
        max-width: 1200px !important;
    }
    #banner-section *, .copy-desktop *, .copy-mobile * {
        color: #0f172a !important;
        -webkit-text-fill-color: #0f172a !important;
        text-shadow: none !important;
    }
    #banner-section h1 {
        font-size: 32px !important;
        font-weight: 800 !important;
        margin-bottom: 12px !important;
    }
    #banner-section p {
        font-size: 16px !important;
        color: #475569 !important;
        -webkit-text-fill-color: #475569 !important;
    }

    /* 3. Cards & Sections */
    .card-pencarian, .card-base-pmb, .card-berita, .card-pilihan-jalur, .card-metode-pembayaran, .card-user-guide {
        background: #ffffff !important;
        border: 2px solid #0f172a !important;
        border-radius: 10px !important;
        box-shadow: none !important;
    }
    .card-base-pmb * {
        color: #0f172a !important;
    }

    /* 4. Buttons */
    .button-pmb_primary, button[type="submit"] {
        background: #0f172a !important;
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        border: 2px solid #0f172a !important;
        border-radius: 8px !important;
        font-weight: 700 !important;
    }
    .button-pmb_primary * {
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
    }
    .button-pmb_primary-outline {
        background: #ffffff !important;
        color: #0f172a !important;
        -webkit-text-fill-color: #0f172a !important;
        border: 2px solid #0f172a !important;
        border-radius: 8px !important;
        font-weight: 700 !important;
    }
    .tag-category.active, .tag-category {
        background: #ffffff !important;
        color: #0f172a !important;
        -webkit-text-fill-color: #0f172a !important;
        border: 1.5px solid #0f172a !important;
        border-radius: 6px !important;
    }

    /* 5. Inputs */
    .form-pmb select, .form-pmb input, .select2-container--default .select2-selection--single {
        background: #ffffff !important;
        border: 1.5px solid #64748b !important;
        border-radius: 6px !important;
        color: #0f172a !important;
    }

    /* 6. FAQ Accordion */
    #faq-section {
        background: #ffffff !important;
        border-top: 2px dashed #94a3b8 !important;
        border-bottom: 2px dashed #94a3b8 !important;
    }
    .faq-header span {
        background: #f1f5f9 !important;
        color: #0f172a !important;
        border: 1.5px solid #0f172a !important;
    }
    .faq-header h2 {
        color: #0f172a !important;
    }
    .faq-card {
        background: #ffffff !important;
        border: 2px solid #0f172a !important;
        border-radius: 8px !important;
        margin-bottom: 12px !important;
    }
    .faq-btn {
        background: #f8fafc !important;
        border: none !important;
        font-weight: 700 !important;
        color: #0f172a !important;
    }
    .faq-collapse {
        background: #ffffff !important;
        border-top: 1px dashed #cbd5e1 !important;
        color: #334155 !important;
    }

    /* 7. Contact Card */
    .card-contact-us {
        background: #f8fafc !important;
        background-image: none !important;
        border: 2.5px solid #0f172a !important;
        border-radius: 14px !important;
        box-shadow: none !important;
    }
    .card-contact-us h1 {
        color: #0f172a !important;
        font-weight: 800 !important;
    }
    .card-contact-us p {
        color: #475569 !important;
    }
    .card-contact-us #btn-whatsapp {
        background: #0f172a !important;
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        border: 2px solid #0f172a !important;
        border-radius: 8px !important;
    }
    .card-contact-us #btn-whatsapp * {
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
    }
    .card-contact-us #btn-user-guide {
        background: #ffffff !important;
        color: #0f172a !important;
        -webkit-text-fill-color: #0f172a !important;
        border: 2px solid #0f172a !important;
        border-radius: 8px !important;
    }

    /* 8. Floating Button */
    #okewa-floating_cta {
        background: #0f172a !important;
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        border: 2px solid #000000 !important;
        border-radius: 50px !important;
    }
    #okewa-floating_cta * {
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
    }

    /* 9. Images */
    img:not(.info-kampus-logo img) {
        filter: grayscale(100%) contrast(120%) brightness(95%) !important;
        border: 1.5px dashed #64748b !important;
    }

    /* 10. Footer */
    .footer__landingpage, .botfooter {
        background: #ffffff !important;
        border-top: 2px solid #0f172a !important;
        color: #0f172a !important;
    }
    .footer__landingpage * {
        color: #475569 !important;
    }
</style>
"""

pages = [
    ("index.html", "01_Beranda_Wireframe.png", 1200, 2800),
    ("jalur-seleksi.html", "02_Jalur_Pendaftaran_Wireframe.png", 1200, 2400),
    ("program-studi.html", "03_Program_Studi_Wireframe.png", 1200, 2400),
    ("program-studi-detail-55202.html", "04_Detail_Prodi_TI_Wireframe.png", 1200, 2400),
    ("pengumuman.html", "05_Informasi_Pengumuman_Wireframe.png", 1200, 2400),
    ("detail-pengumuman-10.html", "06_Detail_Pengumuman_Wireframe.png", 1200, 2400),
    ("login.html", "07_Login_Masuk_Wireframe.png", 1200, 2400),
    ("user-guide.html", "08_Petunjuk_Pendaftaran_Wireframe.png", 1200, 2400),
]

temp_html_files = []

for src_html, out_png_name, w, h in pages:
    src_path = os.path.join(project_dir, src_html)
    with open(src_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Clean banner styles
    html = re.sub(r'#banner-section\s*\{[^}]*\}', '', html)

    if "</head>" in html:
        html_wf = html.replace("</head>", wireframe_css + "\n</head>", 1)
    else:
        html_wf = wireframe_css + html

    tmp_name = f"wf_tmp_{src_html}"
    tmp_path = os.path.join(project_dir, tmp_name)
    temp_html_files.append(tmp_path)
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(html_wf)

    temp_screenshot = os.path.join(project_dir, f"tmp_{out_png_name}")
    final_out_path = os.path.join(out_dir, out_png_name)

    print(f"Generating wireframe for {src_html}...")
    cmd = [
        chrome_path,
        "--headless",
        "--no-sandbox",
        "--disable-gpu",
        f"--window-size={w},{h}",
        f"--screenshot={temp_screenshot}",
        f"http://localhost:8080/{tmp_name}"
    ]
    subprocess.run(cmd, check=True)

    # Convert to pure 8-bit grayscale with contrast
    im = Image.open(temp_screenshot)
    gray_im = im.convert("L")
    enhancer = ImageEnhance.Contrast(gray_im)
    final_im = enhancer.enhance(1.15)
    final_im.save(final_out_path)

    # Cleanup temp screenshot
    if os.path.exists(temp_screenshot):
        os.remove(temp_screenshot)

    print(f"-> Saved: {out_png_name}")
    time.sleep(0.5)

# Cleanup temp html files
for tf in temp_html_files:
    if os.path.exists(tf):
        os.remove(tf)

print("\nALL 8 BLACK & WHITE WIREFRAMES GENERATED SUCCESSFULLY IN WIREFRAME_HITAM_PUTIH!")
