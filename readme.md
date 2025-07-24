# 🧠 CritiCheck – Academic Paper Review Automation

CritiCheck is an AI-powered academic paper analysis tool that automatically reviews research papers and generates a well-structured PDF feedback report. It helps students, researchers, and educators improve the quality and credibility of academic writing.

---

## 📌 Features

- 📄 **PDF Extraction**: Extracts plain text from any academic research PDF.
- 🤖 **AI-Based Critique**: Uses LLM (Google Gemini) to analyze structure, references, logic, and plagiarism risks.
- 🧾 **Formatted Feedback**: Outputs a clean, readable PDF with the AI’s suggestions and quality score.
- ✅ **fPDF2-Compatible Text**: Ensures the feedback is formatted safely for Unicode PDF rendering.

---

## 📁 Project Structure


---

## 🚀 How It Works

1. User provides a research paper in PDF format.
2. `extract_text.py` extracts text from the file.
3. The extracted content is passed to a prompt-driven LLM (via `llm_engine.py`) for review.
4. The LLM returns feedback — covering plagiarism, citation quality, logic, clarity, and final score.
5. The feedback is passed to `format_pdf.py` to generate a clean `feedback_report.pdf`.

---

## 🧠 Prompt-Based Review Logic

The tool performs:
- ✅ **Plagiarism Check**
- ✅ **Citation & Reference Validation**
- ✅ **Reference Improvement Suggestions**
- ✅ **Logical Flow & Consistency Review**
- ✅ **Grammar & Clarity Suggestions**
- ✅ **Final Scoring + Department Classification**

The LLM is instructed to:
- Avoid non-ASCII characters
- Keep line lengths short
- Limit feedback to under 1000 words

---

## 🛠️ Requirements

- Python 3.8+
- Packages:
  ```bash
  pip install -r requirements.txt
