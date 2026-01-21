"""Tests for scripture_slides.utils module."""

import logging
from pathlib import Path
from scripture_slides.utils import (
    get_config_dir,
    get_config_file,
    get_log_file,
    sanitize_filename,
    setup_logging,
)


def test_get_config_dir():
    """Test that get_config_dir returns correct path."""
    config_dir = get_config_dir()
    assert isinstance(config_dir, Path)
    assert config_dir == Path.home() / ".scripture-slides"


def test_get_config_file():
    """Test that get_config_file returns correct path."""
    config_file = get_config_file()
    assert isinstance(config_file, Path)
    assert config_file == Path.home() / ".scripture-slides" / "config.yaml"


def test_get_log_file():
    """Test that get_log_file returns correct path."""
    log_file = get_log_file()
    assert isinstance(log_file, Path)
    assert log_file == Path.home() / ".scripture-slides" / "scripture-slides.log"


def test_sanitize_filename_replaces_spaces():
    """Test that sanitize_filename replaces spaces with underscores."""
    result = sanitize_filename("John 3:16")
    assert " " not in result
    assert result == "John_3_16"


def test_sanitize_filename_removes_colons():
    """Test that sanitize_filename replaces colons."""
    result = sanitize_filename("John 3:16-21")
    assert ":" not in result
    assert result == "John_3_16-21"


def test_sanitize_filename_removes_commas():
    """Test that sanitize_filename removes commas."""
    result = sanitize_filename("John 3:16, Romans 8:28")
    assert "," not in result
    assert result == "John_3_16_Romans_8_28"


def test_sanitize_filename_removes_semicolons():
    """Test that sanitize_filename removes semicolons."""
    result = sanitize_filename("Text; with; semicolons")
    assert ";" not in result
    assert result == "Text_with_semicolons"


def test_sanitize_filename_complex_reference():
    """Test sanitize_filename with complex scripture reference."""
    result = sanitize_filename("Matthew 5:1-12, Luke 6:20-23")
    assert result == "Matthew_5_1-12_Luke_6_20-23"


def test_setup_logging_returns_logger():
    """Test that setup_logging returns a logger instance."""
    logger = setup_logging()
    assert isinstance(logger, logging.Logger)
    assert logger.name == "scripture_slides"


def test_setup_logging_sets_debug_level():
    """Test that setup_logging sets DEBUG level."""
    logger = setup_logging()
    assert logger.level == logging.DEBUG


def test_setup_logging_has_handlers():
    """Test that setup_logging configures handlers."""
    logger = setup_logging()
    # Should have at least file handler and console handler
    assert len(logger.handlers) >= 2

    # Check handler types
    handler_types = [type(h).__name__ for h in logger.handlers]
    assert "FileHandler" in handler_types
    assert "StreamHandler" in handler_types
