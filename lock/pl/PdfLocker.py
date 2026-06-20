from pathlib import Path

from pypdf import PdfReader, PdfWriter
from PyQt6.QtCore import pyqtSignal, QObject

from bl.lockPdf import lock_pdf


class PdfLocker(QObject):
    """
    Wrapper object for business logic to use PyQt signals
    """
    finished = pyqtSignal(bool)  # True = success, False = fail

    def lock_pdf(self, path: str, password: str) -> None:
        """
        Wrapper that locks pdf and emits signal with result

        :param path: path to original file
        :param password: selected password
        :return: None
        """
        self.finished.emit(lock_pdf(path, password))