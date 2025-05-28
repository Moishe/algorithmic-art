# ABOUTME: Unit tests for the main CLI interface
# ABOUTME: Tests command line argument parsing and integration with art algorithms

import pytest
import subprocess
import sys
import os
from unittest.mock import patch, MagicMock
import tempfile


def test_main_cli_koch_snowflake():
    """Test CLI interface for koch-snowflake algorithm"""
    with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as tmp:
        try:
            result = subprocess.run([
                sys.executable, "main.py", "koch-snowflake",
                "--detail-level", "3",
                "--size", "400",
                "--output", tmp.name
            ], capture_output=True, text=True)
            
            assert result.returncode == 0
            assert os.path.exists(tmp.name)
            assert os.path.getsize(tmp.name) > 0
        finally:
            if os.path.exists(tmp.name):
                os.unlink(tmp.name)


def test_main_cli_missing_arguments():
    """Test CLI interface with missing required arguments"""
    result = subprocess.run([
        sys.executable, "main.py", "koch-snowflake"
    ], capture_output=True, text=True)
    
    assert result.returncode != 0


def test_main_cli_invalid_algorithm():
    """Test CLI interface with invalid algorithm name"""
    with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as tmp:
        try:
            result = subprocess.run([
                sys.executable, "main.py", "invalid-algorithm",
                "--detail-level", "3",
                "--size", "400", 
                "--output", tmp.name
            ], capture_output=True, text=True)
            
            assert result.returncode != 0
        finally:
            if os.path.exists(tmp.name):
                os.unlink(tmp.name)