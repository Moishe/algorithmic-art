# ABOUTME: Integration tests for the complete art generation workflow
# ABOUTME: Tests end-to-end functionality from CLI to image generation

import pytest
import subprocess
import sys
import os
import tempfile
from PIL import Image


def test_koch_snowflake_integration():
    """Test complete workflow for Koch snowflake generation"""
    with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as tmp:
        try:
            # Run the CLI command
            result = subprocess.run([
                sys.executable, "main.py", "koch-snowflake",
                "--recursion-depth", "3",
                "--size", "300", 
                "--output", tmp.name
            ], capture_output=True, text=True)
            
            # Check command succeeded
            assert result.returncode == 0
            assert result.stderr == ""
            
            # Check file was created and has content
            assert os.path.exists(tmp.name)
            assert os.path.getsize(tmp.name) > 0
            
            # Verify it's a valid image
            with Image.open(tmp.name) as img:
                assert img.format == 'JPEG'
                assert img.size == (300, 300)
                
        finally:
            if os.path.exists(tmp.name):
                os.unlink(tmp.name)


def test_sierpinski_gasket_integration():
    """Test complete workflow for Sierpinski gasket generation"""
    with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as tmp:
        try:
            # Run the CLI command
            result = subprocess.run([
                sys.executable, "main.py", "sierpinski-gasket",
                "--recursion-depth", "3",
                "--size", "300", 
                "--output", tmp.name
            ], capture_output=True, text=True)
            
            # Check command succeeded
            assert result.returncode == 0
            assert result.stderr == ""
            
            # Check file was created and has content
            assert os.path.exists(tmp.name)
            assert os.path.getsize(tmp.name) > 0
            
            # Verify it's a valid image
            with Image.open(tmp.name) as img:
                assert img.format == 'JPEG'
                assert img.size == (300, 300)
                
        finally:
            if os.path.exists(tmp.name):
                os.unlink(tmp.name)


def test_different_detail_levels():
    """Test that different detail levels produce different results"""
    with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as tmp1, \
         tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as tmp2:
        try:
            # Generate snowflake with depth 1
            subprocess.run([
                sys.executable, "main.py", "koch-snowflake",
                "--recursion-depth", "1",
                "--size", "200",
                "--output", tmp1.name
            ], check=True)
            
            # Generate snowflake with depth 2
            subprocess.run([
                sys.executable, "main.py", "koch-snowflake", 
                "--recursion-depth", "2",
                "--size", "200",
                "--output", tmp2.name
            ], check=True)
            
            # Files should be different sizes (more detail = more complex image)
            size1 = os.path.getsize(tmp1.name)
            size2 = os.path.getsize(tmp2.name)
            assert size1 != size2
            
        finally:
            for tmp in [tmp1, tmp2]:
                if os.path.exists(tmp.name):
                    os.unlink(tmp.name)


def test_sierpinski_arrowhead_integration():
    """Test complete workflow for Sierpinski arrowhead generation"""
    with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as tmp:
        try:
            # Run the CLI command
            result = subprocess.run([
                sys.executable, "main.py", "sierpinski-arrowhead",
                "--recursion-depth", "3",
                "--size", "300", 
                "--output", tmp.name
            ], capture_output=True, text=True)
            
            # Check command succeeded
            assert result.returncode == 0
            assert result.stderr == ""
            
            # Check file was created and has content
            assert os.path.exists(tmp.name)
            assert os.path.getsize(tmp.name) > 0
            
            # Verify it's a valid image
            with Image.open(tmp.name) as img:
                assert img.format == 'JPEG'
                assert img.size == (300, 300)
                
        finally:
            if os.path.exists(tmp.name):
                os.unlink(tmp.name)


def test_mandelbrot_set_integration():
    """Test complete workflow for Mandelbrot set generation"""
    with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as tmp:
        try:
            # Run the CLI command
            result = subprocess.run([
                sys.executable, "main.py", "mandelbrot-set",
                "--num-iterations", "50",
                "--size", "200", 
                "--output", tmp.name
            ], capture_output=True, text=True)
            
            # Check command succeeded
            assert result.returncode == 0
            assert result.stderr == ""
            
            # Check file was created and has content
            assert os.path.exists(tmp.name)
            assert os.path.getsize(tmp.name) > 0
            
            # Verify it's a valid image
            with Image.open(tmp.name) as img:
                assert img.format == 'JPEG'
                assert img.size == (200, 200)
                
        finally:
            if os.path.exists(tmp.name):
                os.unlink(tmp.name)