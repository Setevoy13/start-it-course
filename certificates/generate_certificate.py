#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse, os, json
from datetime import date
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from reportlab.graphics.barcode import qr

def load_config(path="config.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def color_hex(c):
    return colors.HexColor(c)

def ensure_font(font_path):
    try:
        pdfmetrics.registerFont(TTFont("UNI", font_path))
        return "UNI"
    except Exception:
        return "Helvetica"

def draw_frame(c, w, h, primary, accent):
    c.setStrokeColor(color_hex(primary))
    c.setLineWidth(16)
    c.rect(20, 20, w-40, h-40)
    c.setStrokeColor(color_hex(accent))
    c.setLineWidth(4)
    c.rect(40, 40, w-80, h-80)

def draw_logo(c, w, h, logo_path):
    if logo_path and os.path.exists(logo_path):
        img = ImageReader(logo_path)
        c.drawImage(img, w-5*cm, h-4*cm, 4*cm, 3*cm, preserveAspectRatio=True, mask='auto')
        c.saveState()
        c.translate(w/2, h/2)
        c.rotate(30)
        try:
            c.setFillAlpha(0.08)
        except Exception:
            pass
        c.drawImage(img, -7*cm, -6*cm, 14*cm, 12*cm, preserveAspectRatio=True, mask='auto')
        c.restoreState()

def draw_signature(c, w, h, signature_path, stamp_path, font, lang):
    # signature line
    c.setFont(font, 12)
    c.setFillColor(colors.black)
    c.line(w-8*cm, 3.2*cm, w-3*cm, 3.2*cm)
    c.drawRightString(w-3*cm, 2.5*cm, ("Signature" if lang=="en" else "Подпись"))
    # signature image
    if signature_path and os.path.exists(signature_path):
        img = ImageReader(signature_path)
        c.drawImage(img, w-8*cm, 3.3*cm, 5*cm, 2.5*cm, preserveAspectRatio=True, mask='auto')
    # stamp
    if stamp_path and os.path.exists(stamp_path):
        img = ImageReader(stamp_path)
        c.drawImage(img, 2*cm, 1.5*cm, 3*cm, 3*cm, preserveAspectRatio=True, mask='auto')

def draw_qr(c, w, h, url):
    if not url: 
        return
    code = qr.QrCodeWidget(url)
    bounds = code.getBounds()
    size = 2.5*cm
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]
    from reportlab.graphics.shapes import Drawing
    d = Drawing(size, size, transform=[size/width,0,0,size/height,0,0])
    d.add(code)
    from reportlab.graphics import renderPDF
    renderPDF.draw(d, c, 3*cm, 2*cm)

def generate_certificate(name, lang="en", course=None, issuer=None, layout="portrait", cfg_path="config.json", out="certificate.pdf"):
    cfg = load_config(cfg_path)
    issuer = issuer or cfg.get("issuer","Start IT")
    if course is None:
        course = cfg.get("course_default_en") if lang=="en" else cfg.get("course_default_ru")
    primary = cfg["colors"]["primary"]; accent = cfg["colors"]["accent"]
    font = ensure_font(cfg["font"])

    page = A4 if layout == "portrait" else landscape(A4)
    w, h = page
    c = canvas.Canvas(out, pagesize=page)

    draw_frame(c, w, h, primary, accent)
    draw_logo(c, w, h, cfg.get("logo"))

    # Title
    c.setFillColor(color_hex(primary))
    c.setFont(font, 26)
    title = "CERTIFICATE OF COMPLETION" if lang=="en" else "СЕРТИФИКАТ О ПРОХОЖДЕНИИ"
    c.drawCentredString(w/2, h-4.2*cm, title)

    # Subtitle
    c.setFillColor(color_hex(cfg["colors"]["muted"]))
    c.setFont(font, 14)
    sub = "This certifies that" if lang=="en" else "Настоящим подтверждается, что"
    c.drawCentredString(w/2, h-5.2*cm, sub)

    # Name
    c.setFillColor(colors.black)
    c.setFont(font, 32)
    c.drawCentredString(w/2, h-6.5*cm, name)

    # Body
    c.setFillColor(color_hex("#334155"))
    c.setFont(font, 14)
    line = "has successfully completed the course" if lang=="en" else "успешно завершил(а) курс"
    c.drawCentredString(w/2, h-7.7*cm, line)
    c.setFillColor(colors.black)
    c.setFont(font, 18)
    c.drawCentredString(w/2, h-8.7*cm, course)

    # Date
    today = date.today().strftime("%B %d, %Y") if lang=="en" else date.today().strftime("%d.%m.%Y")
    c.setFillColor(colors.black); c.setFont(font, 12)
    c.line(3*cm, 3.2*cm, 8*cm, 3.2*cm)
    c.drawString(3*cm, 2.5*cm, ("Date: " if lang=="en" else "Дата: ") + today)

    # Signature & stamp
    draw_signature(c, w, h, cfg.get("signature"), cfg.get("stamp"), font, lang)

    # QR code
    draw_qr(c, w, h, cfg.get("verify_url"))

    # Footer
    c.setFillColor(color_hex("#64748b"))
    c.setFont(font, 9)
    c.drawCentredString(w/2, 1.2*cm, f"{issuer} • Free & Open Source — github.com/your-org/start-it")
    c.showPage(); c.save()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True, help="Student full name")
    ap.add_argument("--lang", choices=["en","ru"], default="en", help="Certificate language")
    ap.add_argument("--course", help="Course title (optional)")
    ap.add_argument("--issuer", help="Issuer (optional)")
    ap.add_argument("--layout", choices=["portrait","landscape"], default="portrait", help="Page layout")
    ap.add_argument("--config", default="config.json", help="Path to config.json")
    ap.add_argument("--out", default="certificate.pdf", help="Output PDF path")
    args = ap.parse_args()
    generate_certificate(args.name, args.lang, args.course, args.issuer, args.layout, args.config, args.out)

if __name__ == "__main__":
    main()
