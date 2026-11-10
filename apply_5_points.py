import os
import re

# 1. Update program-studi.html (Point 1: Jelas Informasi Jalur Reguler)
prodi_html_path = "program-studi.html"
with open(prodi_html_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace general "Tersedia X Jalur Pendaftaran" with informative badges
old_desc_pattern = r'<div class="description">\s*Tersedia \d+ Jalur Pendaftaran\s*</div>'
new_desc = """<div class="description" style="margin-top: 8px; display: flex; align-items: center; gap: 8px; flex-wrap: wrap;">
                                                    <span style="background: rgba(29, 143, 225, 0.12); color: #1d8fe1; font-weight: 700; font-size: 11.5px; padding: 4px 10px; border-radius: 6px;">Jalur Reguler (Dibuka)</span>
                                                    <span style="background: rgba(37, 211, 102, 0.14); color: #15803d; font-weight: 700; font-size: 11.5px; padding: 4px 10px; border-radius: 6px;">Beasiswa KIP-Kuliah</span>
                                                    <span style="color: #64748b; font-size: 12px; font-weight: 600;">Gelombang 1 T.A 2026/2027</span>
                                                </div>"""

content = re.sub(old_desc_pattern, new_desc, content)

with open(prodi_html_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated program-studi.html with Jalur Reguler & Beasiswa badges!")

# 2. Update program-studi-detail-55202.html (Point 3: Sinkronisasi Jalur & Point 4: Materi Perkuliahan)
detail_path = "program-studi-detail-55202.html"
with open(detail_path, "r", encoding="utf-8") as f:
    d_content = f.read()

# Add Materi Perkuliahan tab button in nav
if 'href="#materi"' not in d_content:
    d_content = d_content.replace(
        '<a class="nav-link" href="#jalur">Jalur Pendaftaran</a>',
        '<a class="nav-link" href="#materi">Materi & Kurikulum</a></li>\n                                    <li class="nav-item"><a class="nav-link" href="#jalur">Jalur Pendaftaran</a>'
    )

# Section Materi Perkuliahan HTML
materi_section = """
<!-- POINT 4: MATERI PERKULIAHAN & MATA KULIAH UTAMA -->
<div class="line-bold"></div>
<div id="materi" style="padding: 30px 0 20px;">
    <div style="margin-bottom: 24px;">
        <span style="background: rgba(29, 143, 225, 0.12); color: #1d8fe1; font-weight: 700; font-size: 12px; text-transform: uppercase; letter-spacing: 0.8px; padding: 5px 14px; border-radius: 50px;">Gambaran Pembelajaran</span>
        <h2 style="font-size: 24px; font-weight: 800; color: #0f172a; margin-top: 10px; margin-bottom: 8px;">Materi Perkuliahan & Mata Kuliah Utama</h2>
        <p style="color: #64748b; font-size: 14.5px; line-height: 1.6; margin: 0; max-width: 800px;">Kurikulum S1 Teknik Informatika UMNU Kebumen dirancang berbasis kebutuhan industri teknologi modern dan standar Aptikom, mencakup 4 pilar kompetensi utama yang dipelajari selama perkuliahan:</p>
    </div>

    <div class="row g-3">
        <!-- Pilar 1 -->
        <div class="col-12 col-md-6 mb-3">
            <div style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 14px; padding: 22px; height: 100%; box-shadow: 0 4px 12px rgba(15,23,42,0.03);">
                <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px;">
                    <div style="width: 44px; height: 44px; border-radius: 10px; background: rgba(29, 143, 225, 0.12); display: flex; align-items: center; justify-content: center; color: #1d8fe1;">
                        <span class="material-icons-round" style="font-size: 24px;">code</span>
                    </div>
                    <div>
                        <h3 style="font-size: 16px; font-weight: 700; color: #0f172a; margin: 0;">1. Software Engineering & Pemrograman</h3>
                        <span style="font-size: 12px; color: #64748b;">Pengembangan Aplikasi Web & Mobile</span>
                    </div>
                </div>
                <p style="font-size: 13.5px; color: #475569; line-height: 1.6; margin-bottom: 12px;">Mempelajari logika algoritma, rekayasa perangkat lunak, pemrograman berorientasi objek, serta arsitektur web modern full-stack.</p>
                <div style="display: flex; flex-wrap: wrap; gap: 6px;">
                    <span style="font-size: 11.5px; background: #f1f5f9; color: #334155; padding: 4px 10px; border-radius: 6px; font-weight: 600;">Algoritma & Struktur Data</span>
                    <span style="font-size: 11.5px; background: #f1f5f9; color: #334155; padding: 4px 10px; border-radius: 6px; font-weight: 600;">Pemrograman Web (JS/Python/PHP)</span>
                    <span style="font-size: 11.5px; background: #f1f5f9; color: #334155; padding: 4px 10px; border-radius: 6px; font-weight: 600;">Mobile Apps Development</span>
                </div>
            </div>
        </div>

        <!-- Pilar 2 -->
        <div class="col-12 col-md-6 mb-3">
            <div style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 14px; padding: 22px; height: 100%; box-shadow: 0 4px 12px rgba(15,23,42,0.03);">
                <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px;">
                    <div style="width: 44px; height: 44px; border-radius: 10px; background: rgba(139, 92, 246, 0.12); display: flex; align-items: center; justify-content: center; color: #8b5cf6;">
                        <span class="material-icons-round" style="font-size: 24px;">smart_toy</span>
                    </div>
                    <div>
                        <h3 style="font-size: 16px; font-weight: 700; color: #0f172a; margin: 0;">2. Basis Data & Artificial Intelligence (AI)</h3>
                        <span style="font-size: 12px; color: #64748b;">Pengolahan Data & Kecerdasan Buatan</span>
                    </div>
                </div>
                <p style="font-size: 13.5px; color: #475569; line-height: 1.6; margin-bottom: 12px;">Mempelajari pemodelan database relasional dan NoSQL, teknik analisis data, kecerdasan buatan terapan, dan machine learning.</p>
                <div style="display: flex; flex-wrap: wrap; gap: 6px;">
                    <span style="font-size: 11.5px; background: #f1f5f9; color: #334155; padding: 4px 10px; border-radius: 6px; font-weight: 600;">Sistem Basis Data (SQL/NoSQL)</span>
                    <span style="font-size: 11.5px; background: #f1f5f9; color: #334155; padding: 4px 10px; border-radius: 6px; font-weight: 600;">Kecerdasan Buatan (AI)</span>
                    <span style="font-size: 11.5px; background: #f1f5f9; color: #334155; padding: 4px 10px; border-radius: 6px; font-weight: 600;">Data Science & Analitika</span>
                </div>
            </div>
        </div>

        <!-- Pilar 3 -->
        <div class="col-12 col-md-6 mb-3">
            <div style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 14px; padding: 22px; height: 100%; box-shadow: 0 4px 12px rgba(15,23,42,0.03);">
                <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px;">
                    <div style="width: 44px; height: 44px; border-radius: 10px; background: rgba(16, 185, 129, 0.12); display: flex; align-items: center; justify-content: center; color: #10b981;">
                        <span class="material-icons-round" style="font-size: 24px;">lan</span>
                    </div>
                    <div>
                        <h3 style="font-size: 16px; font-weight: 700; color: #0f172a; margin: 0;">3. Jaringan Komputer & Cloud Infrastructure</h3>
                        <span style="font-size: 12px; color: #64748b;">Infrastruktur Server & Jaringan</span>
                    </div>
                </div>
                <p style="font-size: 13.5px; color: #475569; line-height: 1.6; margin-bottom: 12px;">Konfigurasi routing dan switching, administrasi server Linux/Windows, arsitektur komputasi awan (Cloud), dan internet of things.</p>
                <div style="display: flex; flex-wrap: wrap; gap: 6px;">
                    <span style="font-size: 11.5px; background: #f1f5f9; color: #334155; padding: 4px 10px; border-radius: 6px; font-weight: 600;">Jaringan Komputer (Mikrotik/Cisco)</span>
                    <span style="font-size: 11.5px; background: #f1f5f9; color: #334155; padding: 4px 10px; border-radius: 6px; font-weight: 600;">Sistem Operasi & Server Linux</span>
                    <span style="font-size: 11.5px; background: #f1f5f9; color: #334155; padding: 4px 10px; border-radius: 6px; font-weight: 600;">Cloud Computing Essentials</span>
                </div>
            </div>
        </div>

        <!-- Pilar 4 -->
        <div class="col-12 col-md-6 mb-3">
            <div style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 14px; padding: 22px; height: 100%; box-shadow: 0 4px 12px rgba(15,23,42,0.03);">
                <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px;">
                    <div style="width: 44px; height: 44px; border-radius: 10px; background: rgba(245, 158, 11, 0.12); display: flex; align-items: center; justify-content: center; color: #d97706;">
                        <span class="material-icons-round" style="font-size: 24px;">security</span>
                    </div>
                    <div>
                        <h3 style="font-size: 16px; font-weight: 700; color: #0f172a; margin: 0;">4. Keamanan Siber & UI/UX Design</h3>
                        <span style="font-size: 12px; color: #64748b;">Cybersecurity & Desain Pengalaman Pengguna</span>
                    </div>
                </div>
                <p style="font-size: 13.5px; color: #475569; line-height: 1.6; margin-bottom: 12px;">Mempelajari konsep keamanan informasi, kriptografi, perlindungan data, serta metodologi riset dan desain antarmuka pengguna (UI/UX).</p>
                <div style="display: flex; flex-wrap: wrap; gap: 6px;">
                    <span style="font-size: 11.5px; background: #f1f5f9; color: #334155; padding: 4px 10px; border-radius: 6px; font-weight: 600;">Dasar Keamanan Siber (Cyber Security)</span>
                    <span style="font-size: 11.5px; background: #f1f5f9; color: #334155; padding: 4px 10px; border-radius: 6px; font-weight: 600;">UI/UX Design & Prototyping</span>
                    <span style="font-size: 11.5px; background: #f1f5f9; color: #334155; padding: 4px 10px; border-radius: 6px; font-weight: 600;">Kriptografi & Etika TI</span>
                </div>
            </div>
        </div>
    </div>
</div>
"""

# Insert before #jalur
if 'id="materi"' not in d_content:
    d_content = d_content.replace('<div class="line-bold"></div>\n                                <div id="jalur">', materi_section + '\n                                <div class="line-bold"></div>\n                                <div id="jalur">')

# 3. Synchronize Jalur in Detail Prodi (Point 3: Sinkronisasi Informasi Jalur Reguler & Beasiswa)
old_jalur_block = """<div class="card-jalur-pendaftaran">
                                                                                            <h6 class="status-dibuka">Dibuka</h6>
                                            
                                            <div class="main-section ">
                                                <div class="left-section">
                                                    <div class="title-jalur-pendaftaran">
                                                        <h1 class="title">PROGRAM INTERNASIONAL - Program Internasional</h1>
                                                        <p class="description">
                                                                                                                    </p>
                                                        <p class="description">
                                                            <strong style="color:#2A2A2C;font-weight:600;">Sistem Kuliah Reguler</strong>
                                                        </p>
                                                    </div>
                                                </div>
                                                <form action="/spmbfront/jalur-seleksi" method="post">
                                                    <div class="right-section">
                                                        <div class="date-price">
                                                            <div class="items">
                                                                <img src="assets/v4/img/landing-page/calendar.svg" alt="">
                                                                <p>1 September 2026 - 30 April 2027</p>
                                                            </div>
                                                            <div class="items">
                                                                <img src="assets/v4/img/landing-page/money.svg" alt="">
                                                                                                                                    <p>Biaya Daftar <span>Gratis</span></p>
                                                                                                                            </div>
                                                        </div>
                                                        <input type="hidden" name="key" value="20271/1/9/1/26">
                                                        <input type="hidden" name="prodipilihan" value="55202">
                                                        <input type="hidden" name="act" value="detail">
                                                                                                                    <button type="submit" class="button button-pmb_primary">Daftar Sekarang</button>
                                                                                                            </div>
                                                </form>
                                            </div>
                                        </div>"""

new_jalur_block = """<!-- JALUR 1: JALUR REGULER (SINKRON DENGAN FAQ ADMIN) -->
                                        <div class="card-jalur-pendaftaran">
                                            <h6 class="status-dibuka" style="background:#1d8fe1;">Dibuka</h6>
                                            <div class="main-section">
                                                <div class="left-section">
                                                    <div class="title-jalur-pendaftaran">
                                                        <h1 class="title">JALUR REGULER GELOMBANG 1 - S1 TEKNIK INFORMATIKA</h1>
                                                        <p class="description">
                                                            <strong style="color:#1d8fe1;font-weight:600;">Sistem Kuliah: Reguler (Tatap Muka & Praktikum Lab Komputer)</strong>
                                                        </p>
                                                        <p style="color: #64748b; font-size: 13.5px; margin-top: 4px;">Terbuka untuk lulusan SMA/SMK/MA sederajat semua jurusan. Tersedia skema cicilan SPP per semester tanpa bunga tambahan.</p>
                                                    </div>
                                                </div>
                                                <div class="right-section">
                                                    <div class="date-price">
                                                        <div class="items">
                                                            <img src="assets/v4/img/landing-page/calendar.svg" alt="">
                                                            <p>1 Januari – 30 April 2026</p>
                                                        </div>
                                                        <div class="items">
                                                            <img src="assets/v4/img/landing-page/money.svg" alt="">
                                                            <p>Biaya Daftar <span>Rp 200.000</span></p>
                                                        </div>
                                                    </div>
                                                    <a href="jalur-seleksi.html" style="text-decoration:none;">
                                                        <button type="button" class="button button-pmb_primary">Daftar Sekarang</button>
                                                    </a>
                                                </div>
                                            </div>
                                        </div>

                                        <!-- JALUR 2: BEASISWA KIP KULIAH -->
                                        <div class="card-jalur-pendaftaran">
                                            <h6 class="status-dibuka" style="background:#16a34a;">Beasiswa</h6>
                                            <div class="main-section">
                                                <div class="left-section">
                                                    <div class="title-jalur-pendaftaran">
                                                        <h1 class="title">JALUR BEASISWA KIP KULIAH & TAHFIDZ</h1>
                                                        <p class="description">
                                                            <strong style="color:#16a34a;font-weight:600;">Bebas Biaya Pendidikan 100% + Bantuan Biaya Hidup Bulanan</strong>
                                                        </p>
                                                        <p style="color: #64748b; font-size: 13.5px; margin-top: 4px;">Khusus pendaftar pemegang KIP/KKS/PKH atau penghafal Al-Qur'an minimal 5 Juz.</p>
                                                    </div>
                                                </div>
                                                <div class="right-section">
                                                    <div class="date-price">
                                                        <div class="items">
                                                            <img src="assets/v4/img/landing-page/calendar.svg" alt="">
                                                            <p>1 Januari – 30 April 2026</p>
                                                        </div>
                                                        <div class="items">
                                                            <img src="assets/v4/img/landing-page/money.svg" alt="">
                                                            <p>Biaya Daftar <span style="color:#16a34a;">Gratis</span></p>
                                                        </div>
                                                    </div>
                                                    <a href="jalur-seleksi.html" style="text-decoration:none;">
                                                        <button type="button" class="button button-pmb_primary" style="background:#16a34a;border-color:#16a34a;">Daftar Beasiswa</button>
                                                    </a>
                                                </div>
                                            </div>
                                        </div>"""

d_content = d_content.replace(old_jalur_block, new_jalur_block)

with open(detail_path, "w", encoding="utf-8") as f:
    f.write(d_content)
print("Updated program-studi-detail-55202.html with Materi Perkuliahan & Synchronized Jalur!")

# Also copy updated HTML to FILE_HTML_UNTUK_IMPORT_FIGMA
targetDir = r"C:\Users\Administrator\Documents\Project\pmb umnu\FILE_HTML_UNTUK_IMPORT_FIGMA"
if os.path.exists(targetDir):
    import shutil
    shutil.copy("program-studi.html", os.path.join(targetDir, "03_Program_Studi.html"))
    shutil.copy("program-studi-detail-55202.html", os.path.join(targetDir, "04_Detail_Prodi_TI.html"))
    print("Synchronized to FILE_HTML_UNTUK_IMPORT_FIGMA!")
