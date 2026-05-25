from pathlib import Path

APP_NAME = "Cclean"
APP_DISPLAY_NAME = "Cclean - C盘清理工具"
APP_VERSION = "0.1.0"

PROJECT_ROOT = Path(__file__).resolve().parent.parent
LOG_DIR = PROJECT_ROOT / "logs"
LOG_FILE = LOG_DIR / "cclean.log"
