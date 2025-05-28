# ABOUTME: Unit tests for the Sierpinski arrowhead fractal algorithm
# ABOUTME: Tests arrowhead curve generation and fractal construction logic

import pytest
import math
from sierpinski_arrowhead import SierpinskiArrowhead


class TestSierpinskiArrowhead:
    
    def test_initial_line_segment(self):
        """Test that initial line segment has correct endpoints"""
        arrowhead = SierpinskiArrowhead(size=300)
        points = arrowhead.get_initial_line()
        
        assert len(points) == 2
        # Should be a horizontal line centered in the image
        p1, p2 = points
        assert p1[1] == p2[1]  # Same y coordinate (horizontal)
        assert p1[0] < p2[0]   # p1 is left of p2
    
    def test_generate_arrowhead_depth_0(self):
        """Test arrowhead generation with depth 0 returns single line"""
        arrowhead = SierpinskiArrowhead(size=300)
        points = arrowhead.generate_arrowhead(depth=0)
        
        # Depth 0 should just be the initial line segment
        assert len(points) == 2
    
    def test_generate_arrowhead_depth_1(self):
        """Test arrowhead generation with depth 1 has correct number of points"""
        arrowhead = SierpinskiArrowhead(size=300)
        points = arrowhead.generate_arrowhead(depth=1)
        
        # Depth 1 should have more than 2 points due to subdivision
        assert len(points) > 2
        # First iteration should create arrowhead pattern
        assert len(points) >= 3
    
    def test_generate_arrowhead_depth_2(self):
        """Test arrowhead generation with depth 2 has more subdivisions"""
        arrowhead = SierpinskiArrowhead(size=300)
        points = arrowhead.generate_arrowhead(depth=2)
        
        # Each subdivision should increase complexity
        assert len(points) > 3
    
    def test_apply_arrowhead_transformation(self):
        """Test arrowhead transformation on a line segment"""
        arrowhead = SierpinskiArrowhead(size=300)
        p1 = (0, 0)
        p2 = (60, 0)  # Horizontal line
        
        new_points = arrowhead.apply_arrowhead_transformation(p1, p2)
        
        # Should return more than 2 points
        assert len(new_points) >= 3
        # First and last points should match original endpoints
        assert new_points[0] == p1
        assert new_points[-1] == p2
    
    def test_save_image_creates_file(self, tmp_path):
        """Test that save_image creates an image file"""
        arrowhead = SierpinskiArrowhead(size=100)
        points = arrowhead.generate_arrowhead(depth=1)
        
        output_file = tmp_path / "test_arrowhead.png"
        arrowhead.save_image(points, str(output_file))
        
        assert output_file.exists()
        assert output_file.stat().st_size > 0