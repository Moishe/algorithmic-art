# ABOUTME: Unit tests for the Mandelbrot set fractal algorithm
# ABOUTME: Tests Mandelbrot set generation and complex number iteration logic

import pytest
import math
from mandelbrot_set import MandelbrotSet


class TestMandelbrotSet:
    
    def test_mandelbrot_iteration_stable_point(self):
        """Test Mandelbrot iteration for a point known to be in the set"""
        mandelbrot = MandelbrotSet(size=300)
        
        # Point (0, 0) should be stable (in the set)
        iterations = mandelbrot.mandelbrot_iteration(0, 0)
        
        # Should reach max iterations without diverging
        assert iterations == mandelbrot.max_iterations
    
    def test_mandelbrot_iteration_divergent_point(self):
        """Test Mandelbrot iteration for a point known to diverge"""
        mandelbrot = MandelbrotSet(size=300)
        
        # Point (2, 2) should diverge quickly
        iterations = mandelbrot.mandelbrot_iteration(2, 2)
        
        # Should diverge before reaching max iterations
        assert iterations < mandelbrot.max_iterations
    
    def test_generate_mandelbrot_set_returns_matrix(self):
        """Test that generate_mandelbrot_set returns a 2D matrix"""
        mandelbrot = MandelbrotSet(size=100)
        result = mandelbrot.generate_mandelbrot_set()
        
        # Should return a matrix with size x size dimensions
        assert len(result) == 100
        assert len(result[0]) == 100
        assert all(len(row) == 100 for row in result)
    
    def test_generate_mandelbrot_set_iteration_values(self):
        """Test that generate_mandelbrot_set returns valid iteration counts"""
        mandelbrot = MandelbrotSet(size=50)
        result = mandelbrot.generate_mandelbrot_set()
        
        # All values should be between 0 and max_iterations
        for row in result:
            for value in row:
                assert 0 <= value <= mandelbrot.max_iterations
    
    def test_coordinate_mapping(self):
        """Test pixel to complex plane coordinate mapping"""
        mandelbrot = MandelbrotSet(size=100)
        
        # Center pixel should map near the center coordinates (-0.5, 0)
        real, imag = mandelbrot.pixel_to_complex(50, 50)
        assert abs(real - mandelbrot.center_real) < 0.1
        assert abs(imag - mandelbrot.center_imag) < 0.1
        
        # Corner pixels should map to expected ranges
        real_min, imag_max = mandelbrot.pixel_to_complex(0, 0)
        real_max, imag_min = mandelbrot.pixel_to_complex(99, 99)
        
        assert real_min < real_max
        assert imag_min < imag_max
    
    def test_save_image_creates_file(self, tmp_path):
        """Test that save_image creates an image file"""
        mandelbrot = MandelbrotSet(size=50)
        mandelbrot_data = mandelbrot.generate_mandelbrot_set()
        
        output_file = tmp_path / "test_mandelbrot.png"
        mandelbrot.save_image(mandelbrot_data, str(output_file))
        
        assert output_file.exists()
        assert output_file.stat().st_size > 0
    
    def test_mandelbrot_set_with_different_size(self):
        """Test Mandelbrot set generation with different image sizes"""
        mandelbrot = MandelbrotSet(size=200)
        result = mandelbrot.generate_mandelbrot_set()
        
        # Should generate correct dimensions
        assert len(result) == 200
        assert len(result[0]) == 200
    
    def test_mandelbrot_set_with_custom_parameters(self):
        """Test Mandelbrot set with custom zoom and center parameters"""
        mandelbrot = MandelbrotSet(size=100, center_real=-0.5, center_imag=0, zoom=1.5)
        result = mandelbrot.generate_mandelbrot_set()
        
        # Should still return valid matrix
        assert len(result) == 100
        assert len(result[0]) == 100