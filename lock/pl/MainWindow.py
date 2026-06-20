import sys

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QLineEdit, QFileDialog, QPushButton, QLabel, QGridLayout, QWidget

from pl.CustomDialog import CustomDialog


class MainWindow(QWidget):
    """
    Main GUI window
    """
    run = pyqtSignal(str,str)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PDF Encryption')

        self._layout = QGridLayout()
        self.setLayout(self._layout)
        self.resize(400, 400)

        self._select_button = QPushButton("Choose PDF File")
        self._select_button.clicked.connect(self._show_dialog)

        self._selected_file_label = QLabel("File path: ")
        self._selected_file_path = QLineEdit()

        self._enter_password_label = QLabel("Password: ")
        self._password = QLineEdit()
        self._password.setEchoMode(QLineEdit.EchoMode.Password)

        self._enter_password2_label = QLabel("Repeat password: ")
        self._password2 = QLineEdit()
        self._password2.setEchoMode(QLineEdit.EchoMode.Password)

        self._show_characters_toggle = False
        self._show_passwords_button = QPushButton("Show password")
        self._show_passwords_button.clicked.connect(self._show_characters)

        self._run_button = QPushButton("Encrypt")
        self._run_button.clicked.connect(self._run)
        self._cancel_button = QPushButton("Cancel")
        self._cancel_button.clicked.connect(self._cancel)

        self._layout.addWidget(self._select_button, 0, 0, 2, 2)

        self._layout.addWidget(self._selected_file_label, 1,0,1,1)
        self._layout.addWidget(self._selected_file_path, 1,1,1,1)

        self._layout.addWidget(self._enter_password_label, 2, 0, 1, 1)
        self._layout.addWidget(self._password, 2, 1, 1, 1)
        self._layout.addWidget(self._enter_password2_label, 3, 0, 1, 1)
        self._layout.addWidget(self._password2, 3, 1, 1, 1)
        self._layout.addWidget(self._show_passwords_button, 4,1,1,1)

        self._layout.addWidget(self._run_button, 5,0,1,1)
        self._layout.addWidget(self._cancel_button, 5, 1, 1, 1)

        self.src_file_path = None

    def set_run_status(self, status):
        status.connect(self.show_run_dialog)

    def show_run_dialog(self, val):
        if val:
            popup = CustomDialog("PDF Encrypted")
            popup.exec()
        else:
            popup = CustomDialog("Cannot encrypt PDF")
            popup.exec()


    def _show_dialog(self) -> None:
        """
        Open select file dialog

        :return: None
        """
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setNameFilter("Documents (*.pdf)")
        if file_dialog.exec():
            self.src_file_path = file_dialog.selectedFiles()[0]
            self._selected_file_path.setText(self.src_file_path)

    def _show_characters(self) -> None:
        """
        Switch text on show_passwords_button and show/hide password(2) characters

        :return: None
        """
        self._show_characters_toggle = not self._show_characters_toggle
        if self._show_characters_toggle:
            self._show_passwords_button.setText("Hide password")
            self._password.setEchoMode(QLineEdit.EchoMode.Normal)
            self._password2.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self._show_passwords_button.setText("Show password")
            self._password.setEchoMode(QLineEdit.EchoMode.Password)
            self._password2.setEchoMode(QLineEdit.EchoMode.Password)

    def _run(self) -> None:
        """
        Run the encryption process.
        Emits the run Signal with encryption operation result

        Check preconditions and return if not met
        :return: None
        """
        if len(self._password.text()) == 0:
            popup = CustomDialog("Please enter password")
            popup.exec()
            return

        if self._password.text() != self._password2.text():
            popup = CustomDialog("Passwords do not match")
            popup.exec()
            return

        if self.src_file_path is None:
            popup = CustomDialog("No file selected")
            popup.exec()
            return

        self.run.emit(self.src_file_path, self._password.text())



    def _cancel(self) -> None:
        sys.exit(0)