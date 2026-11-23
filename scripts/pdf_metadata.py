#!/usr/bin/env python3
"""Set document metadata on exported CV and cover letter PDFs.

Usage:
  python3 pdf_metadata.py FILE.pdf --author "Alex Doe" \
      --subject "Product Designer · Design Systems & AI" \
      --keywords "Product Design, Design Systems, Figma" --lang en

Title defaults to the file name without .pdf; pass --title "Alex Doe · CV" instead. The file is rewritten in place,
keeping its pages, links and tags. Needs pypdf (pip install pypdf).
"""
import argparse
import os
import sys

from pypdf import PdfReader, PdfWriter
from pypdf.generic import BooleanObject, DictionaryObject, NameObject, TextStringObject


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("--author", required=True)
    ap.add_argument("--title")
    ap.add_argument("--subject", default="")
    ap.add_argument("--keywords", default="")
    ap.add_argument("--lang", default="en", help="es, en, en-GB...")
    ap.add_argument("--creator", default="Job Search Kit", help="app the PDF came from, e.g. Figma")
    a = ap.parse_args()

    title = a.title or os.path.splitext(os.path.basename(a.pdf))[0]
    writer = PdfWriter(clone_from=PdfReader(a.pdf))
    meta = {"/Title": title, "/Author": a.author, "/Creator": a.creator}
    if a.subject:
        meta["/Subject"] = a.subject
    if a.keywords:
        meta["/Keywords"] = a.keywords
    writer.add_metadata(meta)

    root = writer._root_object
    root[NameObject("/Lang")] = TextStringObject(a.lang)
    prefs = root.get("/ViewerPreferences")
    prefs = prefs.get_object() if prefs is not None else DictionaryObject()
    prefs[NameObject("/DisplayDocTitle")] = BooleanObject(True)
    root[NameObject("/ViewerPreferences")] = prefs

    tmp = a.pdf + ".tmp"
    with open(tmp, "wb") as f:
        writer.write(f)
    os.replace(tmp, a.pdf)
    print(f"ok: {title}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
