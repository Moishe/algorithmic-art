# ABOUTME: Unit tests for the Sierpinski Gasket fractal algorithm
# ABOUTME: Tests triangle subdivision and fractal generation logic

import pytest
import math
from sierpinski_gasket import SierpinskiGasket


class TestSierpinskiGasket:
    
    def test_initial_triangle_points(self):
        """Test that initial triangle has correct points"""
        gasket = SierpinskiGasket(size=300)
        points = gasket.get_initial_triangle()
        
        assert len(points) == 3
        # Should form an equilateral triangle
        # Check distances between points are roughly equal
        dist1 = math.sqrt((points[1][0] - points[0][0])**2 + (points[1][1] - points[0][1])**2)
        dist2 = math.sqrt((points[2][0] - points[1][0])**2 + (points[2][1] - points[1][1])**2)
        dist3 = math.sqrt((points[0][0] - points[2][0])**2 + (points[0][1] - points[2][1])**2)
        
        assert abs(dist1 - dist2) < 1
        assert abs(dist2 - dist3) < 1
        assert abs(dist1 - dist3) < 1
    
    def test_generate_gasket_depth_0(self):
        """Test gasket generation with depth 0 returns single triangle"""
        gasket = SierpinskiGasket(size=300)
        triangles = gasket.generate_gasket(depth=0)
        
        # Depth 0 should just be the initial triangle
        assert len(triangles) == 1
        assert len(triangles[0]) == 3
    
    def test_generate_gasket_depth_1(self):
        """Test gasket generation with depth 1 has 3 triangles"""
        gasket = SierpinskiGasket(size=300)
        triangles = gasket.generate_gasket(depth=1)
        
        # Depth 1 should have 3 triangles (corners of original)
        assert len(triangles) == 3
        for triangle in triangles:
            assert len(triangle) == 3
    
    def test_generate_gasket_depth_2(self):
        """Test gasket generation with depth 2 has 9 triangles"""
        gasket = SierpinskiGasket(size=300)
        triangles = gasket.generate_gasket(depth=2)
        
        # Each subdivision multiplies by 3
        assert len(triangles) == 9
        for triangle in triangles:
            assert len(triangle) == 3
    
    def test_subdivide_triangle(self):
        """Test triangle subdivision produces 3 corner triangles"""
        gasket = SierpinskiGasket(size=300)
        triangle = [(0, 0), (60, 0), (30, 52)]  # Roughly equilateral
        
        subtriangles = gasket.subdivide_triangle(triangle)
        
        # Should return 3 triangles
        assert len(subtriangles) == 3
        
        # Each subtriangle should have 3 points
        for subtriangle in subtriangles:
            assert len(subtriangle) == 3