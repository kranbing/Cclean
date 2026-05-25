from cclean.logger import get_logger

logger = get_logger(__name__)


class Cleaner:
    def clean(self, selected_items: list) -> None:
        logger.info("Clean requested for %s items, but cleaning is not implemented yet", len(selected_items))
