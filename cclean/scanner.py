from cclean.logger import get_logger

logger = get_logger(__name__)


class Scanner:
    def scan(self) -> list:
        logger.info("Scan requested, but scanning is not implemented yet")
        return []
