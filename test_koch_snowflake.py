# ABOUTME: Unit tests for the Koch snowflake fractal algorithm
# ABOUTME: Tests geometric calculations and fractal generation logic

import pytest
import math
from koch_snowflake import KochSnowflake


class TestKochSnowflake:
    
    def test_initial_triangle_points(self):
        """Test that initial triangle has correct points"""
        koch = KochSnowflake(size=300)
        points = koch.get_initial_triangle()
        
        assert len(points) == 3
        # Should form an equilateral triangle
        # Check distances between points are roughly equal
        dist1 = math.sqrt((points[1][0] - points[0][0])**2 + (points[1][1] - points[0][1])**2)
        dist2 = math.sqrt((points[2][0] - points[1][0])**2 + (points[2][1] - points[1][1])**2)
        dist3 = math.sqrt((points[0][0] - points[2][0])**2 + (points[0][1] - points[2][1])**2)
        
        assert abs(dist1 - dist2) < 1
        assert abs(dist2 - dist3) < 1
        assert abs(dist1 - dist3) < 1
    
    def test_generate_snowflake_points_depth_0(self):
        """Test snowflake generation with depth 0 returns triangle"""
        koch = KochSnowflake(size=300)
        points = koch.generate_snowflake(depth=0)
        
        # Depth 0 should just be the initial triangle
        assert len(points) >= 3
    
    def test_generate_snowflake_points_depth_1(self):
        """Test snowflake generation with depth 1 has more points"""
        koch = KochSnowflake(size=300)
        points_0 = koch.generate_snowflake(depth=0)
        points_1 = koch.generate_snowflake(depth=1)
        
        # Depth 1 should have more points than depth 0
        assert len(points_1) > len(points_0)
    
    def test_apply_koch_transformation(self):
        """Test Koch transformation on a line segment"""
        koch = KochSnowflake(size=300)
        p1 = (0, 0)
        p2 = (30, 0)
        
        new_points = koch.apply_koch_transformation(p1, p2)
        
        # Should return 5 points forming the Koch curve (start, 1/3, peak, 2/3, end)
        assert len(new_points) == 5
        
        # First and last points should be the original endpoints
        assert new_points[0] == p1
        assert new_points[4] == p2