
# PDF-Merger 🧩

**PDF-Merger** is a simple Python utility to merge multiple PDF files into one, effortlessly.  
Just drop your `.pdf` files into the `PDFs/` folder, run the script, and get a merged document in seconds.

---

## 📦 Features

- Auto-detects `.pdf` files in the `PDFs/` folder.
- Merges them in the order they appear.
- Provides clear prompts and helpful error messages.
- Creates the `PDFs/` folder automatically if it doesn't exist.

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

1. Put all your `.pdf` files into the `PDFs/` folder.
2. Run the script:
   ```bash
   python pdf_merger.py
   ```
3. Enter:
   - A name for the merged PDF (without `.pdf`)
   - A folder path to save the output
4. Done! 🎉

---

## 📂 Example

```
📂 Project Folder
├── pdf_merger.py
├── PDFs
│   ├── file1.pdf
│   ├── file2.pdf
```

After running the script, you'll get:

```
✅ Added: PDFs/file1.pdf  
✅ Added: PDFs/file2.pdf  
✅ Merge complete. File saved as: C:\Users\You\Desktop\merged.pdf
```

---

## 🔒 License

MIT License
