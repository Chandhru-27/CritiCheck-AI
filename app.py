from core.llm_engine import run_llm
from scripts.extract_text import extract_test_from_pdf
from scripts.format_pdf import FeedbackPDF

def analyze_report(text : str) -> str:
    prompt = f"""
        You are an expert academic reviewer. Given the following research paper draft, perform a comprehensive validation and feedback process with the following goals:
        Categorize the report based on which department it comes under.

        Important Note: No non printable ASCII characters must be there in the feedback text. dont generate long lines. make the feedback text comaptible to be formatted by fpdf2.

        1. **Plagiarism Check**:
        - Identify any content that appears to be copied or paraphrased from known academic sources.
        - Flag potential unoriginal text with a percentage of similarity (if detectable).

        2. **Citation & Reference Validation**:
        - Detect all cited sources.
        - Check if each citation is properly formatted (APA/MLA/IEEE).
        - Verify the authenticity and credibility of cited sources (e.g., is it from a valid journal or publication?).
        - Highlight any missing citations where claims are made without support.

        3. **Reference Suggestion**:
        - Suggest stronger or more recent references for key claims, especially if current ones are outdated, weak, or non-scholarly.
        - Provide proper citations in standard format.

        4. **Logical Flow & Argument Validation**:
        - Evaluate the logical consistency and structure of the arguments.
        - Identify fallacies, contradictions, or weak assumptions.
        - Highlight disconnected or repetitive sections.

        5. **Readability and Clarity Review**:
        - Provide suggestions to improve clarity, tone, and coherence for an academic audience.
        - Point out grammatical or structural issues.

        6. **Overall Feedback**:
        - Give a summary of strengths, weaknesses, and improvement suggestions.
        - Rate the paper’s academic quality (out of 10) based on originality, clarity, and structure.

        Now analyze the following research paper accordingly:

        IMPORTANT : give a very summarised feedback. not more than 1000 words
        ACADEMIC REPORT: {text}

    """
    
    return run_llm(prompt=prompt)

if __name__ == "__main__":

    text = extract_test_from_pdf("sample_pdf.pdf") # replace with pdf path
    feedback_text = analyze_report(text=text)
    pdf = FeedbackPDF()
    pdf.add_feedback(feedback_text)
    pdf.output("feedback_report.pdf")

