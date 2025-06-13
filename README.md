# PDF-Merger 🧩

**PDF-Merger** is a lightweight Python utility to merge multiple PDF files into a single document, saved directly to your Desktop — no manual path input required.

---

## 📦 Features

- Automatically detects `.pdf` files in the `PDFs/` folder.
- Automatically creates the `PDFs/` folder if missing.
- Merges files in the order they appear in the folder.
- Saves the merged PDF to the actual Desktop path (supports OneDrive or localized folder names).
- Displays clear progress and error messages.

---

## 🛠️ Requirements

- Python 3.x  
- [`PyPDF2`](https://pypi.org/project/PyPDF2/)

Install it via:

```bash
pip install PyPDF2
```

---

## 🚀 How to Use

1. Place your `.pdf` files inside the `PDFs/` folder.
2. Run the script:
   ```bash
   python pdf_merger.py
   ```
3. When prompted, enter a **name** for the merged PDF (without `.pdf`).
4. The output will be saved directly to your Desktop. 🎉

---

## 📂 Example Structure

```
📂 Project Folder
├── pdf_merger.py
├── PDFs
│   ├── file1.pdf
│   ├── file2.pdf
```

After running the script:

```
✅ Added: PDFs/file1.pdf  
✅ Added: PDFs/file2.pdf  
✅ Merged file saved as: C:\Users\YourName\Desktop\merged.pdf
```

(If your Desktop is synced with OneDrive or renamed, the script will still find it correctly.)

---

## 🔒 License

MIT License
