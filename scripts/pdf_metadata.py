#!/usr/bin/env python3
"""Set document metadata on exported CV and cover letter PDFs.

Usage:
  python3 pdf_metadata.py FILE.pdf --author "Alex Doe" \
      --subject "Product Designer · Design Systems & AI" \
      --keywords "Product Design, Design Systems, Figma" --lang en

Title defaults to the file name without .pdf; pass --title "Alex Doe · CV" instead. The file is rewritten in place,
keeping its pages, links and tags. Also rewrites the XMP metadata (Figma puts the frame name there,
with company and date) and removes duplicate objects to keep the file small. Needs pypdf (pip install pypdf).
"""
import argparse
import os
import sys

from pypdf import PdfReader, PdfWriter
from pypdf.generic import BooleanObject, DictionaryObject, NameObject, StreamObject, TextStringObject
from xml.sax.saxutils import escape


def xmp_packet(title, author, subject, keywords, lang, creator, date):
    """XMP metadata that matches the document info. Figma writes its own XMP with the frame name as dc:title,
    and many viewers (Acrobat, Preview, some ATS parsers) read XMP before the info dictionary."""
    e = lambda v: escape(v, {'"': "&quot;"})
    desc = f'<dc:description><rdf:Alt><rdf:li xml:lang="x-default">{e(subject)}</rdf:li></rdf:Alt></dc:description>' if subject else ""
    kw = f"<pdf:Keywords>{e(keywords)}</pdf:Keywords>" if keywords else ""
    return f"""<?xpacket begin="\ufeff" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/"><rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
<rdf:Description rdf:about="" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:xmp="http://ns.adobe.com/xap/1.0/"
 xmlns:pdf="http://ns.adobe.com/pdf/1.3/" xmlns:pdfuaid="http://www.aiim.org/pdfua/ns/id/">
<dc:title><rdf:Alt><rdf:li xml:lang="x-default">{e(title)}</rdf:li></rdf:Alt></dc:title>
<dc:creator><rdf:Seq><rdf:li>{e(author)}</rdf:li></rdf:Seq></dc:creator>{desc}
<dc:language><rdf:Bag><rdf:li>{e(lang)}</rdf:li></rdf:Bag></dc:language>{kw}
<xmp:CreatorTool>{e(creator)}</xmp:CreatorTool><pdf:Producer>{e(creator)}</pdf:Producer>
<xmp:CreateDate>{date}</xmp:CreateDate><xmp:ModifyDate>{date}</xmp:ModifyDate><xmp:MetadataDate>{date}</xmp:MetadataDate>
<pdfuaid:part>1</pdfuaid:part>
</rdf:Description></rdf:RDF></x:xmpmeta>
<?xpacket end="w"?>"""


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
    # Fewer duplicate objects (fonts repeated per page in Figma exports, pages merged from several files)
    writer.compress_identical_objects()
    for page in writer.pages:
        page.compress_content_streams()
    meta = {"/Title": title, "/Author": a.author, "/Creator": a.creator, "/Producer": a.creator}
    if a.subject:
        meta["/Subject"] = a.subject
    if a.keywords:
        meta["/Keywords"] = a.keywords
    writer.add_metadata(meta)

    root = writer._root_object
    import datetime
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    xmp = StreamObject()
    xmp.set_data(xmp_packet(title, a.author, a.subject, a.keywords, a.lang, a.creator, now).encode("utf-8"))
    xmp.update({NameObject("/Type"): NameObject("/Metadata"), NameObject("/Subtype"): NameObject("/XML")})
    root[NameObject("/Metadata")] = writer._add_object(xmp)
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
