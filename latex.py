import shutil
import subprocess
import tempfile
from pathlib import Path
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename


def find_xelatex():
    base = Path(__file__).parent / "TinyTeX" / "bin"

    candidates = [
        base / "windows" / "xelatex.exe",
        base / "win32" / "xelatex.exe",
        base / "x86_64-windows" / "xelatex.exe",
    ]

    for path in candidates:
        if path.exists():
            return path

    return None


def latex_escape(text: str) -> str:
    """
    Escapes LaTeX special characters.
    """

    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text


def compile_memoir_pdf(memoir):
    """
    Generates a PDF from the memoir dictionary.

    Parameters
    ----------
    memoir : dict
        Dictionary returned by extract_memoir_json().
    """

    # -------------------------
    # Ask user where to save
    # -------------------------

    root = Tk()
    root.withdraw()

    output_pdf = asksaveasfilename(
        title="Save Memoir PDF",
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")]
    )

    root.destroy()

    if not output_pdf:
        print("Export cancelled.")
        return

    # -------------------------
    # Load template
    # -------------------------

    template_path = (
        Path(__file__).parent
        / "resources"
        / "template.tex"
    )

    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    # -------------------------
    # Build BODY
    # -------------------------

    body = ""

    for entry in memoir["entries"]:

        body += (
            f"\\chapter*{{{latex_escape(entry['title'])}}}\n\n"
            f"\\textit{{{latex_escape(entry['date'])}}}\n\n"
            f"{latex_escape(entry['contents'])}\n\n"
        )

    tex = template.replace("<<BODY>>", body)

    # -------------------------
    # Temporary build directory
    # -------------------------

    with tempfile.TemporaryDirectory() as tmp:

        tmp = Path(tmp)

        tex_file = tmp / "memoir.tex"

        with open(tex_file, "w", encoding="utf-8") as f:
            f.write(tex)

        # Compile twice
        for _ in range(2):

            xelatex = find_xelatex()

            if not xelatex:
                raise RuntimeError("xelatex not found inside TinyTeX folder")

            subprocess.run(
                [
                    str(xelatex),
                    "-interaction=nonstopmode",
                    tex_file.name
                ],
                cwd=tmp,
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.STDOUT
            )

        generated_pdf = tmp / "memoir.pdf"

        shutil.copy2(
            generated_pdf,
            output_pdf
        )

    print(f"PDF successfully saved to:\n{output_pdf}")
    