import os
import ctypes.wintypes
from PyPDF2 import PdfMerger

PDF_DIR = "PDFs"

def get_desktop_path():
    # Windows Desktop folder ID
    CSIDL_DESKTOP = 0
    SHGFP_TYPE_CURRENT = 0

    buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
    ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_DESKTOP, None, SHGFP_TYPE_CURRENT, buf)
    return buf.value

def get_pdf_files():
    if not os.path.exists(PDF_DIR):
        os.makedirs(PDF_DIR)
        raise FileNotFoundError(
            f"📂 Folder '{PDF_DIR}' created. Add PDFs and rerun."
        )
    if not os.listdir(PDF_DIR):
        raise ValueError(f"📂 Folder '{PDF_DIR}' is empty. Add PDFs and rerun.")

    files = [os.path.join(PDF_DIR, f) for f in os.listdir(PDF_DIR) if f.endswith(".pdf")]
    if not files:
        raise ValueError(f"❌ No PDFs found in '{PDF_DIR}'. Only .pdf files allowed.")
    return files

def merge_pdfs(output_path):
    merger = PdfMerger()
    for pdf_file in get_pdf_files():
        merger.append(pdf_file)
        print(f"✅ Added: {pdf_file}")

    merged_file = f"{output_path}.pdf"
    merger.write(merged_file)
    merger.close()
    print(f"\n✅ Merged file saved as: {merged_file}")


if __name__ == "__main__":
    print(f"📂 Put PDFs to merge inside '{PDF_DIR}' folder.")
    print("📌 Merged PDF will be saved automatically to your Desktop.\n")

    name = input("📝 Merged file name (no .pdf): ").strip()
    desktop = get_desktop_path()
    out_path = os.path.join(desktop, name)

    try:
        merge_pdfs(out_path)
    except Exception as e:
        print(f"\n❌ Error: {e}")
