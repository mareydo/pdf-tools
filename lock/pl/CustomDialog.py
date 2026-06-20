from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel


class CustomDialog(QDialog):
    """
    Simple dialog with custom message
    """
    def __init__(self, msg):
        super().__init__()

        self.setWindowTitle(msg)
        self._layout = QVBoxLayout()

        self.resize(100,100)

        self._message = QLabel(msg)
        self._layout.addWidget(self._message)

        self.setLayout(self._layout)