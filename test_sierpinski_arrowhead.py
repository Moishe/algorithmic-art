# ABOUTME: Unit tests for the Sierpinski arrowhead fractal algorithm
# ABOUTME: Tests arrowhead curve generation and fractal construction logic

import pytest
import math
from sierpinski_arrowhead import SierpinskiArrowhead


class TestSierpinskiArrowhead:
    
    def test_generate_lsystem_string_depth_0(self):
        """Test L-system string generation with depth 0"""
        arrowhead = SierpinskiArrowhead(size=300)
        lsystem_string = arrowhead.generate_lsystem_string(depth=0)
        
        # Depth 0 should just be the axiom "A"
        assert lsystem_string == "A"
    
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
    
    def test_generate_lsystem_string_depth_1(self):
        """Test L-system string generation with depth 1"""
        arrowhead = SierpinskiArrowhead(size=300)
        lsystem_string = arrowhead.generate_lsystem_string(depth=1)
        
        # Depth 1: A -> B-A-B
        assert lsystem_string == "B-A-B"
    
    def test_interpret_turtle_commands_simple(self):
        """Test turtle graphics interpretation with simple commands"""
        arrowhead = SierpinskiArrowhead(size=300, step_length=10)
        start_pos = (100, 100)
        
        # Simple forward movement
        points = arrowhead.interpret_turtle_commands("A", start_pos=start_pos, start_angle=0)
        
        # Should have start point and one forward movement
        assert len(points) == 2
        assert points[0] == start_pos
        # Should move 10 units right (angle 0)
        assert abs(points[1][0] - 110) < 0.1
        assert abs(points[1][1] - 100) < 0.1
    
    def test_save_image_creates_file(self, tmp_path):
        """Test that save_image creates an image file"""
        arrowhead = SierpinskiArrowhead(size=100)
        points = arrowhead.generate_arrowhead(depth=1)
        
        output_file = tmp_path / "test_arrowhead.png"
        arrowhead.save_image(points, str(output_file))
        
        assert output_file.exists()
        assert output_file.stat().st_size > 0