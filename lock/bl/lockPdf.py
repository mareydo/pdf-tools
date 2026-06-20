from pathlib import Path

from pypdf import PdfReader, PdfWriter

def lock_pdf(path: str, password: str) -> bool:
    """
    Create a locked copy of file at {path} as {path}_locked.pdf

    Uses AES-256 same as Adobe

    :param path: path to file
    :param password: selected password for file
    :return: boolean representing success/fail
    """
    try:
        src_path = Path(path)
        out_path = src_path.with_name(f"{src_path.stem}_locked{src_path.suffix}")

        reader = PdfReader(src_path)
        writer = PdfWriter(clone_from=reader)

        writer.encrypt(password, algorithm="AES-256")  # match Adobe

        fout = open(out_path, "wb")
        writer.write(fout)

        return True
    except Exception as e:
        print(f"Error locking PDF: {e}")
        return False