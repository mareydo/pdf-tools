import sys

from PyQt6.QtWidgets import QApplication

from pl.MainWindow import MainWindow
from pl.PdfLocker import PdfLocker

if __name__ == '__main__':
    app = QApplication([])

    main_window = MainWindow()
    pdf_locker = PdfLocker()
    main_window.run.connect(pdf_locker.lock_pdf)
    main_window.set_run_status(pdf_locker.finished)
    main_window.show()

    sys.exit(app.exec())
