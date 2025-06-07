import os
from PyPDF2 import PdfMerger

PDFS_DIR = "PDFs"

def read_pdfs_dir():
    """
    Reads all PDF files from the PDFs folder.

    Returns:
        list[str]: A list of full paths to the .pdf files found in the folder.

    Raises:
        FileNotFoundError: If the PDFs folder does not exist (it will be created).
        ValueError: If the folder is empty or contains no .pdf files.
    """
    if not os.path.exists(PDFS_DIR):
        os.makedirs(PDFS_DIR)
        raise FileNotFoundError(
            f"📂 Folder '{PDFS_DIR}' was created because it didn't exist.\n"
            f"➕ Add PDF files to this folder and restart the program."
        )

    if not os.listdir(PDFS_DIR):
        raise ValueError(
            f"📂 Folder '{PDFS_DIR}' is empty.\n➕ Add PDF files and restart the program."
        )

    pdf_files = [os.path.join(PDFS_DIR, f) for f in os.listdir(PDFS_DIR) if f.endswith(".pdf")]

    if not pdf_files:
        raise ValueError(
            f"❌ No PDF files found in '{PDFS_DIR}'.\nOnly files ending with .pdf are processed."
        )

    return pdf_files


def merge_pdfs(output_filepath):
    """
    Merges all PDF files from the PDFs folder into a single file.

    Args:
        output_filepath (str): Full path (excluding the .pdf extension) for the output file.
    """
    merger = PdfMerger()
    for pdf in read_pdfs_dir():
        merger.append(pdf)
        print(f"✅ Added: {pdf}")

    merged_file = f"{output_filepath}.pdf"
    merger.write(merged_file)
    merger.close()
    print(f"\n✅ Merge complete. File saved as: {merged_file}")




if __name__ == "__main__":
    """
    Entry point of the program.

    Prompts the user to enter:
    - A name for the merged PDF (without extension)
    - A folder path to save the output

    Then merges all PDFs from the PDFs directory and saves the result.
    """
    print(f"📂 Place all PDF files you want to merge inside the '{PDFS_DIR}' folder.")
    print("📌 Example output path: C:\\Users\\YourName\\Desktop\n")

    file_name = input("📝 Enter a name for the merged file (without .pdf): ").strip()
    save_path = input("📁 Enter the folder path to save the merged file: ").strip()

    output_filepath = rf"{save_path}\{file_name}"

    try:
        merge_pdfs(output_filepath)
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
