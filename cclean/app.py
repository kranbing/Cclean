from PySide6.QtWidgets import QApplication

from cclean.config import APP_NAME
from cclean.logger import configure_logging, get_logger
from cclean.ui.main_window import MainWindow
from cclean.ui.styles import load_stylesheet


def main() -> int:
    configure_logging()
    logger = get_logger(__name__)
    logger.info("Starting %s", APP_NAME)

    app = QApplication([])
    app.setApplicationName(APP_NAME)
    app.setStyleSheet(load_stylesheet())

    window = MainWindow()
    window.show()

    exit_code = app.exec()
    logger.info("%s exited with code %s", APP_NAME, exit_code)
    return exit_code
