import os
from PyPDF2 import PdfMerger

PDF_DIR = "PDFs"

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
    print("📌 Example save path: C:\\Users\\YourName\\Desktop\n")

    name = input("📝 Merged file name (no .pdf): ").strip()
    folder = input("📁 Save folder path: ").strip()

    out_path = rf"{folder}\{name}"

    try:
        merge_pdfs(out_path)
    except Exception as e:
        print(f"\n❌ Error: {e}")
