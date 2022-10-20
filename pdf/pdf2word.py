from pathlib import Path
from pdf2docx import parse

file = Path("11.pdf").resolve()


parse(str(file), f"{file.parent.resolve()}/{file.name}.docx")