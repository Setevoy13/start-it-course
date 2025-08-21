#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv, os, argparse, subprocess

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", default="students.csv", help="CSV with columns: name,lang,course(optional),issuer(optional),out(optional),layout(optional)")
    ap.add_argument("--outdir", default="output")
    ap.add_argument("--config", default="config.json")
    args = ap.parse_args()

    os.makedirs(args.outdir, exist_ok=True)
    with open(args.csv, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for i,row in enumerate(reader, start=1):
            name = row.get("name","").strip()
            lang = (row.get("lang","en") or "en").strip()
            course = row.get("course") or ""
            issuer = row.get("issuer") or ""
            out = row.get("out", f"{name.replace(' ','_')}.pdf")
            layout = row.get("layout", "portrait")
            out_path = os.path.join(args.outdir, out)
            cmd = ["python", "generate_certificate.py", "--name", name, "--lang", lang, "--layout", layout, "--config", args.config, "--out", out_path]
            if course: cmd += ["--course", course]
            if issuer: cmd += ["--issuer", issuer]
            print(f"[{i}] Generating:", " ".join(cmd))
            subprocess.check_call(cmd)

if __name__ == "__main__":
    main()
