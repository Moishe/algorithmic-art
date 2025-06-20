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
                "--recursion-depth", "3",
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


def test_main_cli_sierpinski_gasket():
    """Test CLI interface for sierpinski-gasket algorithm"""
    with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as tmp:
        try:
            result = subprocess.run([
                sys.executable, "main.py", "sierpinski-gasket",
                "--recursion-depth", "3",
                "--size", "400",
                "--output", tmp.name
            ], capture_output=True, text=True)
            
            assert result.returncode == 0
            assert os.path.exists(tmp.name)
            assert os.path.getsize(tmp.name) > 0
        finally:
            if os.path.exists(tmp.name):
                os.unlink(tmp.name)


def test_main_cli_sierpinski_arrowhead():
    """Test CLI interface for sierpinski-arrowhead algorithm"""
    with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as tmp:
        try:
            result = subprocess.run([
                sys.executable, "main.py", "sierpinski-arrowhead",
                "--recursion-depth", "3",
                "--size", "400",
                "--output", tmp.name
            ], capture_output=True, text=True)
            
            assert result.returncode == 0
            assert os.path.exists(tmp.name)
            assert os.path.getsize(tmp.name) > 0
        finally:
            if os.path.exists(tmp.name):
                os.unlink(tmp.name)


def test_main_cli_mandelbrot_set():
    """Test CLI interface for mandelbrot-set algorithm"""
    with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as tmp:
        try:
            result = subprocess.run([
                sys.executable, "main.py", "mandelbrot-set",
                "--num-iterations", "50",
                "--size", "200",
                "--output", tmp.name
            ], capture_output=True, text=True)
            
            assert result.returncode == 0
            assert os.path.exists(tmp.name)
            assert os.path.getsize(tmp.name) > 0
        finally:
            if os.path.exists(tmp.name):
                os.unlink(tmp.name)


def test_main_cli_invalid_algorithm():
    """Test CLI interface with invalid algorithm name"""
    result = subprocess.run([
        sys.executable, "main.py", "invalid-algorithm"
    ], capture_output=True, text=True)
    
    assert result.returncode != 0
    assert "No such command 'invalid-algorithm'" in result.stderr