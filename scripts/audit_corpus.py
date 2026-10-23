import glob
import os

files = sorted(glob.glob("docs/*.md"))
total_chars = 0
short_docs = []
medium_docs = []
long_docs = []

for f in files:
    content = open(f, encoding="utf-8").read()
    chars = len(content)
    total_chars += chars
    name = os.path.basename(f)
    if chars < 2100:
        short_docs.append((name, chars))
    elif chars > 5500:
        long_docs.append((name, chars))
    else:
        medium_docs.append((name, chars))

print("=" * 60)
print("NexaTech Solutions - Document Corpus Audit (Phase 0)")
print("=" * 60)
print(f"Total Documents: {len(files)}")
print(f"Total Character Count: {total_chars:,} characters")
print(f"Estimated Pages: {round(total_chars / 2500, 1)} - {round(total_chars / 3000, 1)} pages (approx. 100-150 standard pages)")
print("-" * 60)
print(f"Short Documents (under 1 page): {len(short_docs)}")
for name, chars in short_docs[:5]:
    print(f"  - {name}: {chars} chars")
print("-" * 60)
print(f"Long Documents (8-15 pages / deep reference): {len(long_docs)}")
for name, chars in long_docs:
    print(f"  - {name}: {chars} chars")
print("-" * 60)
print(f"Medium Documents (2-5 pages): {len(medium_docs)}")
print("=" * 60)
