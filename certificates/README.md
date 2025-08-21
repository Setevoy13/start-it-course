# Start IT — Certificate Kit v5 (Pro Edition)

Professional, configurable certificate generator (EN/RU) with logo, signature image, stamp, QR code, portrait/landscape layouts, batch mode and GitHub Actions.

## Quick Start
```bash
pip install reportlab

# single
python generate_certificate.py --name "John Smith" --lang en --layout portrait --out output/John_Smith.pdf

# batch
python generate_batch.py --csv students.csv --outdir output
```
> Tip: Edit `config.json` to change colors, issuer, verify URL, and assets.

## Config (`config.json`)
- `issuer`: footer issuer text
- `course_default_en` / `course_default_ru`: default course titles
- `colors.primary` / `colors.accent` / `colors.muted`
- `logo`, `signature`, `stamp`, `font`
- `verify_url`: URL encoded into QR code (e.g., verification page or your repo)

## GitHub Actions
Workflow at `.github/workflows/certificate.yml` lets you generate a certificate from the UI:
- Inputs: name, language, course, issuer, layout
- Output: PDF as an artifact

## Assets
- `assets/logo.png` — replace with your brand
- `assets/signature.png` — scanned signature (PNG, transparent)
- `assets/stamp.png` — official stamp/seal (PNG, transparent)
- `assets/DejaVuSans.ttf` — Unicode font
- `assets/sample_design_en.png`, `assets/sample_design_ru.png` — design previews
