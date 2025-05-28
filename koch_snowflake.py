# ABOUTME: Implementation of the Koch snowflake fractal algorithm
# ABOUTME: Generates fractal curves and renders them to image files

import math
from PIL import Image, ImageDraw


class KochSnowflake:
    def __init__(self, size):
        self.size = size
        
    def get_initial_triangle(self):
        """Generate an equilateral triangle as the base for the Koch snowflake"""
        center_x = self.size // 2
        center_y = self.size // 2
        radius = self.size * 0.35  # Leave some margin
        
        # Calculate points of equilateral triangle
        points = []
        for i in range(3):
            angle = i * 2 * math.pi / 3 - math.pi / 2  # Start from top
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            points.append((x, y))
            
        return points
    
    def apply_koch_transformation(self, p1, p2):
        """Apply Koch curve transformation to a line segment"""
        x1, y1 = p1
        x2, y2 = p2
        
        # Calculate the four points of the Koch curve
        # First point is the original start
        new_points = [p1]
        
        # Second point is 1/3 along the line
        dx = x2 - x1
        dy = y2 - y1
        x_third = x1 + dx / 3
        y_third = y1 + dy / 3
        new_points.append((x_third, y_third))
        
        # Third point is the peak of the equilateral triangle
        # The peak should form an equilateral triangle with the 1/3 and 2/3 points
        # Calculate the midpoint between 1/3 and 2/3 points
        mid_x = (x_third + (x1 + 2 * dx / 3)) / 2
        mid_y = (y_third + (y1 + 2 * dy / 3)) / 2
        
        # Calculate perpendicular vector (rotate 90 degrees counter-clockwise)
        # This determines which side the triangle points to
        segment_length = math.sqrt(dx*dx + dy*dy) / 3  # Length of middle third
        height = segment_length * math.sqrt(3) / 2  # Height of equilateral triangle
        
        # Perpendicular unit vector (rotate 90 degrees)
        total_length = math.sqrt(dx*dx + dy*dy)
        if total_length > 0:
            # Unit vector perpendicular to the line segment
            # Try the other direction (clockwise rotation)
            unit_perp_x = dy / total_length
            unit_perp_y = -dx / total_length
            
            perp_x = unit_perp_x * height
            perp_y = unit_perp_y * height
        else:
            perp_x = perp_y = 0
        
        peak_x = mid_x + perp_x
        peak_y = mid_y + perp_y
        new_points.append((peak_x, peak_y))
        
        # Fourth point is 2/3 along the original line
        x_two_thirds = x1 + 2 * dx / 3
        y_two_thirds = y1 + 2 * dy / 3
        new_points.append((x_two_thirds, y_two_thirds))
        
        # Fifth point is the original end
        new_points.append(p2)
        
        return new_points
    
    def generate_snowflake(self, depth):
        """Generate Koch snowflake points with given recursion depth"""
        # Start with initial triangle
        points = self.get_initial_triangle()
        
        # Apply Koch transformation for each depth level
        for _ in range(depth):
            new_points = []
            for i in range(len(points)):
                current_point = points[i]
                next_point = points[(i + 1) % len(points)]
                
                # Apply Koch transformation to this edge
                transformed = self.apply_koch_transformation(current_point, next_point)
                
                # Add all but the last point (to avoid duplication when connecting segments)
                new_points.extend(transformed[:-1])
            
            points = new_points
            
        return points
    
    def save_image(self, points, filename):
        """Save the snowflake points as an image"""
        # Create a white image
        image = Image.new('RGB', (self.size, self.size), 'white')
        draw = ImageDraw.Draw(image)
        
        # Convert points to integers for drawing
        int_points = [(int(x), int(y)) for x, y in points]
        
        # Draw the snowflake as connected lines
        if len(int_points) > 1:
            # Draw lines connecting each point to the next
            for i in range(len(int_points)):
                start_point = int_points[i]
                end_point = int_points[(i + 1) % len(int_points)]
                draw.line([start_point, end_point], fill='black', width=2)
        
        # Save the image
        image.save(filename)