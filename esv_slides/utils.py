"""Utility functions for esv-slides."""

import logging
import os
from pathlib import Path


def get_config_dir():
    """Get the config directory path."""
    return Path.home() / ".esv-slides"


def get_config_file():
    """Get the config file path."""
    return get_config_dir() / "config.yaml"


def get_log_file():
    """Get the log file path."""
    return get_config_dir() / "esv-slides.log"


def setup_logging():
    """Set up logging to file and console."""
    log_file = get_log_file()
    log_file.parent.mkdir(parents=True, exist_ok=True)

    # Create logger
    logger = logging.getLogger("esv_slides")
    logger.setLevel(logging.DEBUG)

    # File handler - detailed logging
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(file_formatter)

    # Console handler - only errors
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.ERROR)
    console_formatter = logging.Formatter("%(message)s")
    console_handler.setFormatter(console_formatter)

    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


def sanitize_filename(text):
    """Sanitize text for use in filename.

    Args:
        text: Text to sanitize

    Returns:
        Sanitized text with spaces and special chars replaced
    """
    # Replace spaces and special characters
    text = text.replace(" ", "_")
    text = text.replace(":", "_")
    text = text.replace(",", "")
    text = text.replace(";", "")

    return text
