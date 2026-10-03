from pathlib import Path
import hashlib,json,sys
root=Path(__file__).resolve().parents[1]
manifest=json.loads((root/'provenance/checksums.json').read_text())
errors=[]
for name,digest in manifest.items():
    p=root/name
    if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=digest:
        errors.append(name)
print(f"Checked {len(manifest)} files; failures: {len(errors)}")
for name in errors: print(name)
sys.exit(bool(errors))
