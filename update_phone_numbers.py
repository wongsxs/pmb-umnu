import os
import glob
import re

folders = [
    ".",
    "CLONE_PMB_UMNU_100_PERSIS",
    "UPGRADE UI UX",
    "UPGRADE UI-UX"
]

updated_files = 0

for folder in folders:
    if not os.path.exists(folder):
        continue
    for f in glob.glob(os.path.join(folder, "*.html")):
        if "SHOWCASE" in f:
            continue
        with open(f, 'r', encoding='utf-8') as fp:
            content = fp.read()

        new_content = content
        
        # 1. Update floating WhatsApp link to use the valid international 62 format and friendly text
        new_content = re.sub(
            r'href="https://wa\.me/085216993300[^"]*"',
            'href="https://wa.me/6285216993300?text=Halo%20Admin%20PMB%20UMNU%20Kebumen,%20saya%20ingin%20bertanya%20seputar%20pendaftaran"',
            new_content
        )
        
        # 2. Update footer phone number from inactive 02876601209 to active 0852-1699-3300
        new_content = new_content.replace(
            '02876601209',
            '0852-1699-3300'
        )

        if new_content != content:
            with open(f, 'w', encoding='utf-8') as fp:
                fp.write(new_content)
            updated_files += 1
            print(f"Updated phone/wa in: {f}")

print(f"\nSuccessfully updated phone number & floating WhatsApp across {updated_files} pages!")
