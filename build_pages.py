import os
import glob
import re

replacements = [
    ('https://assets.siakadcloud.com/spmbfront/assets/v4/external/dist/css/bootstrap.min.css', 'assets/v4/external/dist/css/bootstrap.min.css'),
    ('https://assets.siakadcloud.com/spmbfront/assets/v4/external/air-datepicker/css/datepicker.css', 'assets/v4/external/air-datepicker/css/datepicker.css'),
    ('https://assets.siakadcloud.com/spmbfront/assets/v4/../default/css/style.wa.min.css', 'assets/default/css/style.wa.min.css'),
    ('https://assets.siakadcloud.com/spmbfront/assets/default/css/style.wa.min.css', 'assets/default/css/style.wa.min.css'),
    ('https://assets.siakadcloud.com/spmbfront/assets/v4/../default/css/typeahead-bootstrap/typeaheadjs.css', 'assets/default/css/typeahead-bootstrap/typeaheadjs.css'),
    ('https://assets.siakadcloud.com/spmbfront/assets/v4/css/select2.min.css', 'assets/v4/css/select2.min.css'),
    ('https://assets.siakadcloud.com/spmbfront/assets/v4/css/main.css?260421', 'assets/v4/css/main.css'),
    ('https://assets.siakadcloud.com/spmbfront/assets/v4/css/main.css', 'assets/v4/css/main.css'),
    ('https://fastly.jsdelivr.net/npm/lightgallery@1.10.0/dist/css/lightgallery.min.css', 'assets/v4/css/lightgallery.min.css'),
    ('https://assets.siakadcloud.com/uploads/umnu/logoaplikasi/1894.jpg?1771071899', 'uploads/umnu/logoaplikasi/1894.jpg'),
    ('https://assets.siakadcloud.com/uploads/umnu/logoaplikasi/1894.jpg', 'uploads/umnu/logoaplikasi/1894.jpg'),
    ('https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js', 'assets/v4/js/jquery.min.js'),
    ('https://assets.siakadcloud.com/spmbfront/assets/v4/../default/js/jquery.min.js', 'assets/v4/js/jquery.min.js'),
    ('https://assets.siakadcloud.com/spmbfront/assets/v4/../default/js/moment.js', 'assets/default/js/moment.js'),
    ('https://assets.siakadcloud.com/spmbfront/assets/v4/../default/js/bootstrap-datetimepicker.js', 'assets/default/js/bootstrap-datetimepicker.js'),
    ('https://assets.siakadcloud.com/spmbfront/assets/v4/../default/js/jquery-migrate-1.2.1.min.js', 'assets/default/js/jquery-migrate-1.2.1.min.js'),
    ('https://assets.siakadcloud.com/spmbfront/assets/v4/../default/js/id.js', 'assets/default/js/id.js'),
    ('https://cdnjs.cloudflare.com/ajax/libs/bootbox.js/6.0.0/bootbox.js', 'assets/default/js/bootbox.js'),
    ('https://assets.siakadcloud.com/spmbfront/assets/v4/../default/js/bootstrap.min.js', 'assets/v4/external/dist/js/bootstrap.bundle.min.js'),
    ('https://assets.siakadcloud.com/spmbfront/assets/v4/../default/js/jquery-ui-1.10.3.min.js', 'assets/default/js/jquery-ui-1.10.3.min.js'),
    ('https://assets.siakadcloud.com/spmbfront/assets/v4/../default/js/typeahead.jquery.js', 'assets/default/js/typeahead.jquery.js'),
    ('https://assets.siakadcloud.com/spmbfront/assets/v4/../default/js/jquery.ajax.js?210916', 'assets/default/js/jquery.ajax.js'),
    ('https://assets.siakadcloud.com/spmbfront/assets/v4/../default/js/jquery.ajax.js', 'assets/default/js/jquery.ajax.js'),
    ('https://assets.siakadcloud.com/spmbfront/assets/v4/../default/js/forhtml.js?260814', 'assets/default/js/forhtml.js'),
    ('https://assets.siakadcloud.com/spmbfront/assets/v4/../default/js/forhtml.js', 'assets/default/js/forhtml.js'),
    ('https://assets.siakadcloud.com/spmbfront/assets/v4/../default/js/custom.js?260430', 'assets/default/js/custom.js'),
    ('https://assets.siakadcloud.com/spmbfront/assets/v4/../default/js/custom.js', 'assets/default/js/custom.js'),
    ('https://assets.siakadcloud.com/spmbfront/assets/v4/external/air-datepicker/js/datepicker.min.js', 'assets/v4/external/air-datepicker/js/datepicker.min.js'),
    ('https://assets.siakadcloud.com/spmbfront/assets/v4/external/air-datepicker/js/datepicker.id.js', 'assets/v4/external/air-datepicker/js/datepicker.id.js'),
    ('https://assets.siakadcloud.com/spmbfront/assets/v4/js/select2.min.js', 'assets/v4/js/select2.min.js'),
    ('https://assets.siakadcloud.com/spmbfront/assets/v4/external/dist/js/bootstrap.bundle.min.js', 'assets/v4/external/dist/js/bootstrap.bundle.min.js'),
    ('https://assets.siakadcloud.com/spmbfront/assets/v4/js/background-dim.js', 'assets/v4/js/background-dim.js'),
    ('https://fastly.jsdelivr.net/npm/lightgallery@1.10.0/dist/js/lightgallery-all.min.js', 'assets/v4/js/lightgallery-all.min.js'),
    ('/spmbfront/../uploads/umnu/settingsim/163.jpg?59483', 'uploads/umnu/settingsim/163.jpg'),
    ('/spmbfront/../uploads/umnu/settingsim/233.jpg?99094', 'uploads/umnu/settingsim/233.jpg'),
    ('/spmbfront/../uploads/', 'uploads/'),
    ('https://assets.siakadcloud.com/spmbfront/assets/v4/img/landing-page/icon-wa.svg', 'assets/v4/img/landing-page/icon-wa.svg'),
    ('https://assets.siakadcloud.com/spmbfront/assets/v4//img/landing-page/social-media/social-ig.svg', 'assets/v4/img/landing-page/social-media/social-ig.svg'),
    ('https://assets.siakadcloud.com/spmbfront/assets/v4//img/whatsapp-icon.png', 'assets/v4/img/whatsapp-icon.png'),
    ('https://assets.siakadcloud.com/spmbfront/assets/v4/img/landing-page/calendar.svg', 'assets/v4/img/landing-page/calendar.svg'),
    ('https://assets.siakadcloud.com/spmbfront/assets/v4/img/landing-page/icon-home.svg', 'assets/v4/img/landing-page/icon-home.svg'),
    ('https://assets.siakadcloud.com/spmbfront/assets/v4/img/landing-page/money.svg', 'assets/v4/img/landing-page/money.svg'),
    ('https://assets.siakadcloud.com/spmbfront/assets/v4/img/landing-page/jalur-empty.svg', 'assets/v4/img/landing-page/jalur-empty.svg'),
    ('https://assets.siakadcloud.com/spmbfront/assets/v4/img/landing-page/icon-failed.svg', 'assets/v4/img/landing-page/icon-failed.svg'),
    ('https://assets.siakadcloud.com/spmbfront/assets/v4/img/landing-page/icon-facebook.svg', 'assets/v4/img/landing-page/icon-facebook.svg'),
    ('https://assets.siakadcloud.com/spmbfront/assets/v4/img/landing-page/icon-twitter.svg', 'assets/v4/img/landing-page/icon-twitter.svg'),
    ('href="/spmbfront/home"', 'href="index.html"'),
    ('href="/spmbfront/"', 'href="index.html"'),
    ('href="/spmbfront"', 'href="index.html"'),
    ('href="/spmbfront/jalur-seleksi"', 'href="jalur-seleksi.html"'),
    ('href="/spmbfront/program-studi?jenjang=S1"', 'href="program-studi.html?jenjang=S1"'),
    ('href="/spmbfront/program-studi"', 'href="program-studi.html"'),
    ('href="/spmbfront/pengumuman"', 'href="pengumuman.html"'),
    ('href="/spmbfront/login"', 'href="login.html"'),
    ('href="/spmbfront/user-guide"', 'href="user-guide.html"'),
    ('href="/spmbfront/?lang=id"', 'href="?lang=id"'),
    ('href="/spmbfront/?lang=en"', 'href="?lang=en"'),
    ('/spmbfront/detail-pengumuman/10/program-studi-manajemen-haji-dan-umroh', 'detail-pengumuman.html?id=10'),
    ('/spmbfront/detail-pengumuman/8/brosur-dan-informasi-biaya-s2-program-pendidikan-umum-dan-karakter', 'detail-pengumuman.html?id=8'),
    ('/spmbfront/detail-pengumuman/6/cek-desil', 'detail-pengumuman.html?id=6'),
    ('/spmbfront/detail-pengumuman/5/berkas-kip-k', 'detail-pengumuman.html?id=5'),
    ('/spmbfront/detail-pengumuman/7/', 'detail-pengumuman.html?id=7'),
    ('/spmbfront/detail-pengumuman/4/', 'detail-pengumuman.html?id=4'),
    ('/spmbfront/detail-pengumuman/3/', 'detail-pengumuman.html?id=3'),
    ('href="program-studi-detail/detail/55202"', 'href="program-studi-detail.html?id=55202"'),
    ('href="program-studi-detail/detail/89201"', 'href="program-studi-detail.html?id=89201"'),
    ('href="program-studi-detail/detail/88203"', 'href="program-studi-detail.html?id=88203"'),
    ('href="program-studi-detail/detail/86207"', 'href="program-studi-detail.html?id=86207"'),
    ('href="program-studi-detail/detail/93208"', 'href="program-studi-detail.html?id=93208"'),
    ('href="program-studi-detail/detail/87106"', 'href="program-studi-detail.html?id=87106"'),
    ('href="program-studi-detail/detail/54293"', 'href="program-studi-detail.html?id=54293"'),
    ('href="program-studi-detail/detail/79201"', 'href="program-studi-detail.html?id=79201"'),
    ('href="program-studi-detail/detail/54238"', 'href="program-studi-detail.html?id=54238"'),
    ('href="program-studi-detail/detail/22201"', 'href="program-studi-detail.html?id=22201"'),
]

def process_content(content):
    for src, dst in replacements:
        content = content.replace(src, dst)
    return content

def process_file(src_path, dst_path):
    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = process_content(content)
    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Processed {src_path} -> {dst_path}")

# Main pages
process_file('downloaded_index.html', 'index.html')
process_file('jalur-seleksi.html', 'jalur-seleksi.html')
process_file('program-studi.html', 'program-studi.html')
process_file('pengumuman.html', 'pengumuman.html')
process_file('login.html', 'login.html')
process_file('user-guide.html', 'user-guide.html')

# Detail prodi files
for p in glob.glob('prodi-cache/*.html'):
    id_num = os.path.basename(p).replace('.html', '')
    process_file(p, f'program-studi-detail-{id_num}.html')

# Detail pengumuman files
for p in glob.glob('pengumuman-cache/*.html'):
    id_num = os.path.basename(p).replace('.html', '')
    process_file(p, f'detail-pengumuman-{id_num}.html')

# Generate smart router for program-studi-detail.html and detail-pengumuman.html
prodi_router = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Redirecting...</title>
    <script>
        const urlParams = new URLSearchParams(window.location.search);
        const id = urlParams.get('id') || '55202';
        window.location.replace('program-studi-detail-' + id + '.html');
    </script>
</head>
<body>
    <p>Loading...</p>
</body>
</html>
"""
with open('program-studi-detail.html', 'w', encoding='utf-8') as f:
    f.write(prodi_router)

pengumuman_router = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Redirecting...</title>
    <script>
        const urlParams = new URLSearchParams(window.location.search);
        const id = urlParams.get('id') || '10';
        window.location.replace('detail-pengumuman-' + id + '.html');
    </script>
</head>
<body>
    <p>Loading...</p>
</body>
</html>
"""
with open('detail-pengumuman.html', 'w', encoding='utf-8') as f:
    f.write(pengumuman_router)

print("Build complete!")
