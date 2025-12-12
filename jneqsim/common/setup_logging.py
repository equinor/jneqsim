import logging


def setup_logging(config: dict) -> logging.Logger:
    """Setup logging based on configuration"""
    logger = logging.getLogger(__name__)
    level = getattr(logging, config["logging"]["level"])
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
