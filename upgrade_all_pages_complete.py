import os
import glob
import re

css_inject = """
    <!-- 3 UI/UX ENHANCEMENTS: HEADER, FAQ, WHATSAPP & CONTACT -->
    <style type="text/css">
        /* 1. MODERN HEADER */
        .navbar__landingpage {
            background: #ffffff !important;
            box-shadow: 0 4px 20px -2px rgba(15, 23, 42, 0.06) !important;
            border-bottom: 1px solid #eef2f6 !important;
            padding: 12px 0 !important;
            position: sticky !important;
            top: 0 !important;
            z-index: 1000 !important;
        }
        .navbar__landingpage .navbar-info .info-kampus-logo img,
        .info-kampus .info-kampus-logo img,
        .info-kampus-logo img {
            width: 48px !important;
            height: 48px !important;
            border-radius: 50% !important;
            border: 2px solid #e2e8f0 !important;
            box-shadow: 0 2px 6px rgba(0,0,0,0.06) !important;
            transition: transform 0.2s ease !important;
        }
        .navbar__landingpage .navbar-info:hover .info-kampus-logo img {
            transform: scale(1.06) !important;
        }
        .navbar__landingpage .navbar-info .info-kampus-text h1 {
            font-size: 15.5px !important;
            font-weight: 700 !important;
            color: #0f172a !important;
            line-height: 1.25 !important;
            margin: 0 !important;
        }
        .navbar__landingpage .navbar-info .info-kampus-text p {
            font-size: 11px !important;
            font-weight: 600 !important;
            text-transform: uppercase !important;
            letter-spacing: 0.8px !important;
            color: #1d8fe1 !important;
            margin: 0 !important;
        }
        .navbar__landingpage .navbar-menu {
            display: flex !important;
            align-items: center !important;
            gap: 4px !important;
        }
        .navbar__landingpage .navbar-menu li a.navbar-item {
            color: #475569 !important;
            font-size: 13.5px !important;
            font-weight: 600 !important;
            padding: 8px 16px !important;
            border-radius: 8px !important;
            transition: all 0.2s ease !important;
        }
        .navbar__landingpage .navbar-menu li a.navbar-item:hover,
        .navbar__landingpage .navbar-menu li.active a.navbar-item {
            color: #1d8fe1 !important;
            background: rgba(29, 143, 225, 0.08) !important;
        }
        .cta-language {
            background: #f1f5f9 !important;
            border: 1px solid #e2e8f0 !important;
            color: #334155 !important;
            font-size: 13px !important;
            font-weight: 600 !important;
            padding: 7px 12px !important;
            border-radius: 8px !important;
            display: flex !important;
            align-items: center !important;
            gap: 6px !important;
            cursor: pointer !important;
            transition: all 0.2s ease !important;
        }
        .cta-language:hover {
            background: #e2e8f0 !important;
        }
        #dropdown-language .dropdown-menu {
            display: none;
            list-style: none !important;
            padding: 8px 0;
            margin: 0;
        }
        #dropdown-language .dropdown-menu.show {
            display: block;
        }
        #dropdown-language ul {
            list-style: none !important;
            padding-left: 0 !important;
            margin-bottom: 0 !important;
        }

        /* 2. FAQ STYLES */
        .faq-card {
            border: 1.5px solid #e2e8f0 !important;
            border-radius: 12px !important;
            margin-bottom: 14px !important;
            overflow: hidden !important;
            background: #ffffff !important;
            transition: all 0.2s ease !important;
        }
        .faq-card:hover {
            border-color: #1d8fe1 !important;
            box-shadow: 0 4px 16px rgba(29, 143, 225, 0.08) !important;
        }
        .faq-btn {
            width: 100% !important;
            text-align: left !important;
            background: #ffffff !important;
            border: none !important;
            padding: 20px 24px !important;
            font-size: 15.5px !important;
            font-weight: 700 !important;
            color: #1e293b !important;
            display: flex !important;
            align-items: center !important;
            justify-content: space-between !important;
            gap: 16px !important;
            cursor: pointer !important;
            transition: background-color 0.2s ease !important;
        }
        .faq-btn:hover {
            background: #f8fafc !important;
        }
        .faq-btn.active .faq-icon {
            transform: rotate(180deg) !important;
            color: #0b5694 !important;
        }
        .faq-collapse {
            display: none;
            padding: 0 24px 20px !important;
            color: #475569 !important;
            font-size: 14.5px !important;
            line-height: 1.7 !important;
            border-top: 1px solid #f1f5f9 !important;
        }

        /* 3. MODERN WHATSAPP & CONTACT SECTION */
        .card-contact-us {
            background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #0369a1 100%),
                        url("uploads/umnu/settingsim/233.jpg") !important;
            background-size: cover !important;
            background-position: center !important;
            border-radius: 20px !important;
            padding: 45px 50px !important;
            box-shadow: 0 20px 40px -10px rgba(15, 23, 42, 0.35) !important;
            color: #ffffff !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
        }
        .card-contact-us .content-contact h1 {
            font-size: 26px !important;
            font-weight: 800 !important;
            color: #ffffff !important;
            margin-bottom: 10px !important;
            letter-spacing: -0.4px !important;
        }
        .card-contact-us .content-contact p {
            color: #cbd5e1 !important;
            font-size: 14.5px !important;
            line-height: 1.6 !important;
        }
        #btn-whatsapp {
            background: #25D366 !important;
            border: none !important;
            color: #ffffff !important;
            font-size: 14px !important;
            font-weight: 700 !important;
            padding: 12px 24px !important;
            border-radius: 10px !important;
            display: inline-flex !important;
            align-items: center !important;
            gap: 8px !important;
            box-shadow: 0 6px 18px rgba(37, 211, 102, 0.35) !important;
            transition: all 0.25s ease !important;
            cursor: pointer !important;
        }
        #btn-whatsapp:hover {
            background: #20bd5a !important;
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 24px rgba(37, 211, 102, 0.5) !important;
            color: #ffffff !important;
        }
        #btn-user-guide {
            background: rgba(255, 255, 255, 0.15) !important;
            backdrop-filter: blur(8px) !important;
            border: 1.5px solid rgba(255, 255, 255, 0.4) !important;
            color: #ffffff !important;
            font-size: 14px !important;
            font-weight: 600 !important;
            padding: 11px 22px !important;
            border-radius: 10px !important;
            transition: all 0.2s ease !important;
            cursor: pointer !important;
            display: inline-flex !important;
            align-items: center !important;
        }
        #btn-user-guide:hover {
            background: rgba(255, 255, 255, 0.28) !important;
            transform: translateY(-2px) !important;
            color: #ffffff !important;
        }

        /* Floating WhatsApp CTA */
        #okewa-floating_cta {
            background: #25D366 !important;
            box-shadow: 0 8px 24px rgba(37, 211, 102, 0.45) !important;
            border-radius: 50px !important;
            padding: 12px 20px !important;
            display: flex !important;
            align-items: center !important;
            gap: 10px !important;
            font-weight: 700 !important;
            font-size: 13.5px !important;
            color: #ffffff !important;
            transition: transform 0.25s ease, box-shadow 0.25s ease !important;
        }
        #okewa-floating_cta:hover {
            transform: scale(1.05) !important;
            box-shadow: 0 10px 28px rgba(37, 211, 102, 0.6) !important;
        }
    </style>
"""

faq_html = """
<!-- FAQ SECTION -->
<section id="faq-section" style="padding: 70px 0 65px; background: #ffffff;">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-lg-10">
                <div class="faq-header text-center mb-5">
                    <span style="display: inline-block; background: rgba(29, 143, 225, 0.1); color: #1d8fe1; font-weight: 700; font-size: 13px; text-transform: uppercase; letter-spacing: 1px; padding: 6px 18px; border-radius: 50px; margin-bottom: 12px;">Pusat Bantuan & FAQ</span>
                    <h2 style="font-size: 30px; font-weight: 800; color: #0f172a; margin-bottom: 10px; letter-spacing: -0.5px;">Pertanyaan yang Sering Diajukan (FAQ)</h2>
                    <p style="color: #64748b; font-size: 15px; max-width: 650px; margin: 0 auto;">Temukan jawaban cepat seputar jalur penerimaan, beasiswa KIP Kuliah, biaya pendidikan, dan tahapan seleksi di Universitas Ma'arif Nahdlatul Ulama Kebumen.</p>
                </div>

                <div class="faq-accordion" id="faqAccordion">
                    <!-- FAQ 1 -->
                    <div class="faq-card" style="border: 1.5px solid #e2e8f0; border-radius: 12px; margin-bottom: 14px; overflow: hidden; transition: all 0.2s ease;">
                        <button class="faq-btn" type="button" onclick="toggleFaq(this)" style="width: 100%; text-align: left; background: #ffffff; border: none; padding: 20px 24px; font-size: 15.5px; font-weight: 700; color: #1e293b; display: flex; align-items: center; justify-content: space-between; gap: 16px; cursor: pointer;">
                            <span>1. Kapan pendaftaran mahasiswa baru UMNU Kebumen T.A 2026/2027 dibuka?</span>
                            <span class="faq-icon material-icons-round" style="font-size: 24px; color: #1d8fe1; transition: transform 0.25s ease;">expand_more</span>
                        </button>
                        <div class="faq-collapse" style="display: none; padding: 0 24px 20px; color: #475569; font-size: 14.5px; line-height: 1.7; border-top: 1px solid #f1f5f9;">
                            Pendaftaran Mahasiswa Baru (PMB) dibuka sepanjang tahun melalui 3 gelombang seleksi:
                            <ul style="margin: 8px 0 0 20px; padding: 0;">
                                <li><strong>Gelombang 1:</strong> 1 Januari – 30 April 2026 (Potongan UKT & Jalur Beasiswa)</li>
                                <li><strong>Gelombang 2:</strong> 1 Mei – 31 Juli 2026 (Jalur Reguler & Prestasi)</li>
                                <li><strong>Gelombang 3:</strong> 1 Agustus – 30 September 2026 (Gelombang Khusus)</li>
                            </ul>
                        </div>
                    </div>

                    <!-- FAQ 2 -->
                    <div class="faq-card" style="border: 1.5px solid #e2e8f0; border-radius: 12px; margin-bottom: 14px; overflow: hidden; transition: all 0.2s ease;">
                        <button class="faq-btn" type="button" onclick="toggleFaq(this)" style="width: 100%; text-align: left; background: #ffffff; border: none; padding: 20px 24px; font-size: 15.5px; font-weight: 700; color: #1e293b; display: flex; align-items: center; justify-content: space-between; gap: 16px; cursor: pointer;">
                            <span>2. Apa saja jalur seleksi yang tersedia di UMNU Kebumen?</span>
                            <span class="faq-icon material-icons-round" style="font-size: 24px; color: #1d8fe1; transition: transform 0.25s ease;">expand_more</span>
                        </button>
                        <div class="faq-collapse" style="display: none; padding: 0 24px 20px; color: #475569; font-size: 14.5px; line-height: 1.7; border-top: 1px solid #f1f5f9;">
                            UMNU Kebumen menyediakan beberapa jalur masuk:
                            <ul style="margin: 8px 0 0 20px; padding: 0;">
                                <li><strong>Jalur Reguler:</strong> Untuk lulusan SMA/SMK/MA/Sederajat tanpa batasan tahun kelulusan.</li>
                                <li><strong>Jalur Beasiswa KIP Kuliah:</strong> Bebas biaya kuliah 100% dan mendapat bantuan biaya hidup bulanan.</li>
                                <li><strong>Jalur Beasiswa Tahfidz & Prestasi:</strong> Potongan biaya kuliah bagi penghafal Al-Qur'an dan pemenang lomba kejuaraan.</li>
                                <li><strong>Jalur RPL (Rekognisi Pembelajaran Lampau):</strong> Konversi SKS bagi lulusan Diploma atau pekerja yang ingin lanjut S1.</li>
                            </ul>
                        </div>
                    </div>

                    <!-- FAQ 3 -->
                    <div class="faq-card" style="border: 1.5px solid #e2e8f0; border-radius: 12px; margin-bottom: 14px; overflow: hidden; transition: all 0.2s ease;">
                        <button class="faq-btn" type="button" onclick="toggleFaq(this)" style="width: 100%; text-align: left; background: #ffffff; border: none; padding: 20px 24px; font-size: 15.5px; font-weight: 700; color: #1e293b; display: flex; align-items: center; justify-content: space-between; gap: 16px; cursor: pointer;">
                            <span>3. Bagaimana tahapan pendaftaran secara online?</span>
                            <span class="faq-icon material-icons-round" style="font-size: 24px; color: #1d8fe1; transition: transform 0.25s ease;">expand_more</span>
                        </button>
                        <div class="faq-collapse" style="display: none; padding: 0 24px 20px; color: #475569; font-size: 14.5px; line-height: 1.7; border-top: 1px solid #f1f5f9;">
                            Pendaftaran online dapat diselesaikan dalam 4 tahapan mudah:
                            <ol style="margin: 8px 0 0 20px; padding: 0;">
                                <li>Buka menu <strong>Jalur Pendaftaran</strong> dan klik <em>Daftar Sekarang</em>.</li>
                                <li>Isi formulir biodata diri dan buat akun pendaftar online.</li>
                                <li>Lakukan pembayaran biaya pendaftaran via Virtual Account / transfer bank.</li>
                                <li>Login ke portal pendaftaran, unggah berkas persyaratan (KTP, KK, Ijazah), dan tunggu pengumuman kelulusan.</li>
                            </ol>
                        </div>
                    </div>

                    <!-- FAQ 4 -->
                    <div class="faq-card" style="border: 1.5px solid #e2e8f0; border-radius: 12px; margin-bottom: 14px; overflow: hidden; transition: all 0.2s ease;">
                        <button class="faq-btn" type="button" onclick="toggleFaq(this)" style="width: 100%; text-align: left; background: #ffffff; border: none; padding: 20px 24px; font-size: 15.5px; font-weight: 700; color: #1e293b; display: flex; align-items: center; justify-content: space-between; gap: 16px; cursor: pointer;">
                            <span>4. Apakah biaya kuliah di UMNU Kebumen bisa diangsur?</span>
                            <span class="faq-icon material-icons-round" style="font-size: 24px; color: #1d8fe1; transition: transform 0.25s ease;">expand_more</span>
                        </button>
                        <div class="faq-collapse" style="display: none; padding: 0 24px 20px; color: #475569; font-size: 14.5px; line-height: 1.7; border-top: 1px solid #f1f5f9;">
                            <strong>Ya, sangat bisa!</strong> UMNU Kebumen memiliki skema pembayaran angsuran bertahap setiap semester tanpa bunga tambahan, demi memastikan pendidikan tinggi dapat dijangkau oleh seluruh lapisan masyarakat.
                        </div>
                    </div>

                    <!-- FAQ 5 -->
                    <div class="faq-card" style="border: 1.5px solid #e2e8f0; border-radius: 12px; margin-bottom: 14px; overflow: hidden; transition: all 0.2s ease;">
                        <button class="faq-btn" type="button" onclick="toggleFaq(this)" style="width: 100%; text-align: left; background: #ffffff; border: none; padding: 20px 24px; font-size: 15.5px; font-weight: 700; color: #1e293b; display: flex; align-items: center; justify-content: space-between; gap: 16px; cursor: pointer;">
                            <span>5. Kemana saya bisa menghubungi panitia jika butuh bantuan?</span>
                            <span class="faq-icon material-icons-round" style="font-size: 24px; color: #1d8fe1; transition: transform 0.25s ease;">expand_more</span>
                        </button>
                        <div class="faq-collapse" style="display: none; padding: 0 24px 20px; color: #475569; font-size: 14.5px; line-height: 1.7; border-top: 1px solid #f1f5f9;">
                            Anda dapat langsung berkonsultasi dengan Panitia PMB melalui <strong>WhatsApp Center: 0852-1699-3300</strong> (Fast Response) atau berkunjung langsung ke Kantor PMB Gedung Rektorat UMNU Kebumen (Senin - Sabtu pukul 08.00 - 16.00 WIB).
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
"""

contact_html = """<section id="contact-us" class="d-none d-sm-block d-md-block">
    <div class="container">
        <div class="row">
            <div class="col-lg-12 nopadding">
                <div class="card-contact-us">
                    <div class="row align-items-center">
                        <div class="col-12 col-lg-7 col-xl-7">
                            <div class="content-contact">
                                <h1>Kami Siap Membantu Anda</h1>
                                <p>Apabila kamu memiliki kendala atau pertanyaan seputar PMB UMNU Kebumen, silakan hubungi kami melalui WhatsApp atau baca Petunjuk Pendaftaran terlebih dahulu.</p>
                            </div>
                        </div>
                        <div class="col-12 col-lg-5 col-xl-5">
                            <div class="cta" style="display: flex; align-items: center; justify-content: flex-end; gap: 12px; flex-wrap: wrap;">
                                <a target="_blank" href="https://wa.me/6285216993300?text=Halo%20Admin%20PMB%20UMNU%20Kebumen,%20saya%20ingin%20bertanya%20seputar%20pendaftaran" style="text-decoration: none;">
                                    <button id="btn-whatsapp" type="button"><img src="assets/v4/img/landing-page/icon-wa.svg" alt="" style="width: 18px; height: 18px; filter: brightness(0) invert(1);"> WhatsApp (0852-1699-3300)</button>
                                </a>
                                <a href="user-guide.html" style="text-decoration: none;">
                                    <button id="btn-user-guide" type="button"><span class="material-icons-round" style="font-size: 18px; margin-right: 6px; vertical-align: middle;">menu_book</span> Petunjuk Pendaftaran</button>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>"""

faq_script = """
    <script>
        function toggleFaq(btn) {
            const collapse = btn.nextElementSibling;
            const icon = btn.querySelector('.faq-icon');
            const isOpen = collapse.style.display === 'block';

            // Close all
            document.querySelectorAll('.faq-collapse').forEach(el => el.style.display = 'none');
            document.querySelectorAll('.faq-btn').forEach(b => {
                b.classList.remove('active');
                if (b.querySelector('.faq-icon')) {
                    b.querySelector('.faq-icon').style.transform = 'rotate(0deg)';
                }
            });

            if (!isOpen) {
                collapse.style.display = 'block';
                btn.classList.add('active');
                if (icon) {
                    icon.style.transform = 'rotate(180deg)';
                }
            }
        }
    </script>
"""

new_cta_navbar = """<div class="cta-navbar" style="display: flex; align-items: center; gap: 8px;">
                            <a href="login.html" style="text-decoration: none;">
                                <button class="button-pmb_primary-outline ripple" style="border-radius: 8px; font-weight: 600; padding: 7px 16px;">Masuk</button>
                            </a>
                            <a href="jalur-seleksi.html" style="text-decoration: none;">
                                <button class="button-pmb_primary ripple" style="border-radius: 8px; font-weight: 600; padding: 8px 18px; box-shadow: 0 4px 12px rgba(29, 143, 225, 0.3);">Daftar</button>
                            </a>
                        </div>"""

def upgrade_page(file_path):
    if not os.path.exists(file_path):
        return
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Skip files that are not full pages
    if "navbar__landingpage" not in content and "<nav" not in content:
        return

    # 1. Inject CSS if not present
    if "3 UI/UX ENHANCEMENTS: HEADER, FAQ, WHATSAPP & CONTACT" not in content:
        if "</head>" in content:
            content = content.replace("</head>", css_inject + "\n</head>", 1)

    # 2. Add FAQ item to navbar menu if not present
    if 'href="#faq-section"' not in content and 'href="index.html#faq-section"' not in content:
        content = re.sub(
            r'(<li class="[^"]*"><a class="navbar-item" href="pengumuman\.html">Informasi</a></li>)',
            r'\1\n                            <li class=""><a class="navbar-item" href="#faq-section">FAQ</a></li>',
            content
        )
        content = re.sub(
            r'(<ul class="navbar-mobile navbar-menu">.*?<a class="navbar-item" href="pengumuman\.html">Informasi</a></li>)',
            r'\1\n                            <li class=""><a class="navbar-item" href="#faq-section">FAQ</a></li>',
            content,
            flags=re.DOTALL
        )

    # 3. Upgrade CTA navbar to dual Masuk + Daftar buttons
    if 'button-pmb_primary ripple' not in content:
        content = re.sub(
            r'<div class="cta-navbar">\s*<a href="login\.html">\s*<button class="button-pmb_primary-outline ripple"[^>]*>Masuk</button>\s*</a>\s*</div>',
            new_cta_navbar,
            content
        )

    # 4. Insert FAQ section before #contact-us if not present
    if 'id="faq-section"' not in content and '<section id="contact-us"' in content:
        content = re.sub(
            r'(<section id="contact-us")',
            faq_html + r'\n\1',
            content,
            count=1
        )

    # 5. Replace #contact-us section with modern markup
    if '<section id="contact-us"' in content:
        content = re.sub(
            r'<section id="contact-us".*?</section>',
            contact_html,
            content,
            count=1,
            flags=re.DOTALL
        )

    # 6. Inject toggleFaq script before </body>
    if "function toggleFaq" not in content:
        if "</body>" in content:
            content = content.replace("</body>", faq_script + "\n</body>", 1)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Successfully upgraded: {file_path}")

target_folders = [
    ".",
    "CLONE_PMB_UMNU_100_PERSIS",
    "UPGRADE UI UX",
    "UPGRADE UI-UX"
]

total_count = 0
for folder in target_folders:
    if not os.path.exists(folder):
        continue
    for html_file in glob.glob(os.path.join(folder, "*.html")):
        if "SHOWCASE" not in html_file and "detail-pengumuman.html" not in html_file and "program-studi-detail.html" not in html_file:
            upgrade_page(html_file)
            total_count += 1

print(f"\nAll done! Successfully upgraded {total_count} pages across all folders.")
