from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QPushButton,
    QProgressBar,
    QPlainTextEdit,
    QVBoxLayout,
    QWidget,
)

from cclean.config import APP_DISPLAY_NAME, APP_VERSION
from cclean.permissions import is_running_as_admin


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle(APP_DISPLAY_NAME)
        self.resize(980, 640)
        self._build_ui()

    def _build_ui(self) -> None:
        root = QWidget()
        layout = QHBoxLayout(root)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(16)

        self.nav_list = QListWidget()
        self.nav_list.setFixedWidth(180)
        for item_text in ("快速清理", "高级清理", "清理日志", "设置"):
            self.nav_list.addItem(QListWidgetItem(item_text))
        self.nav_list.setCurrentRow(0)

        content = QWidget()
        content_layout = QVBoxLayout(content)
        content_layout.setSpacing(12)

        title = QLabel("C盘清理")
        title.setObjectName("PageTitle")

        permission_text = "管理员权限：是" if is_running_as_admin() else "管理员权限：否"
        status = QLabel(f"版本 {APP_VERSION} | {permission_text}")
        status.setObjectName("StatusText")

        description = QLabel("第一阶段已完成基础窗口搭建。扫描和清理功能将在后续阶段接入。")
        description.setWordWrap(True)

        self.scan_button = QPushButton("扫描 C 盘")
        self.scan_button.setEnabled(False)

        self.clean_button = QPushButton("开始清理")
        self.clean_button.setEnabled(False)

        button_row = QWidget()
        button_layout = QHBoxLayout(button_row)
        button_layout.setContentsMargins(0, 0, 0, 0)
        button_layout.addWidget(self.scan_button)
        button_layout.addWidget(self.clean_button)
        button_layout.addStretch(1)

        self.result_list = QListWidget()
        self.result_list.addItem("等待接入扫描模块")

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.progress_bar.setAlignment(Qt.AlignCenter)

        self.log_output = QPlainTextEdit()
        self.log_output.setReadOnly(True)
        self.log_output.setPlaceholderText("清理日志将在这里显示")

        content_layout.addWidget(title)
        content_layout.addWidget(status)
        content_layout.addWidget(description)
        content_layout.addWidget(button_row)
        content_layout.addWidget(self.result_list, 2)
        content_layout.addWidget(self.progress_bar)
        content_layout.addWidget(self.log_output, 1)

        layout.addWidget(self.nav_list)
        layout.addWidget(content, 1)

        self.setCentralWidget(root)
