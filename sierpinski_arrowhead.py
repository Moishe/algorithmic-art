# ABOUTME: Implementation of the Sierpinski arrowhead fractal algorithm
# ABOUTME: Generates arrowhead curve fractals and renders them to image files

import math
from PIL import Image, ImageDraw


class SierpinskiArrowhead:
    def __init__(self, size):
        self.size = size
        
    def get_initial_line(self):
        """Generate initial horizontal line segment for the arrowhead"""
        center_y = self.size // 2
        margin = self.size * 0.15
        start_x = margin
        end_x = self.size - margin
        
        return [(start_x, center_y), (end_x, center_y)]
    
    def apply_arrowhead_transformation(self, p1, p2):
        """Apply arrowhead transformation to a line segment"""
        x1, y1 = p1
        x2, y2 = p2
        
        # Calculate the direction and length of the segment
        dx = x2 - x1
        dy = y2 - y1
        length = math.sqrt(dx*dx + dy*dy)
        
        if length == 0:
            return [p1, p2]
            
        # Normalize direction vector
        unit_x = dx / length
        unit_y = dy / length
        
        # Calculate perpendicular vector (90 degrees counterclockwise)
        perp_x = -unit_y
        perp_y = unit_x
        
        # Points along the original line at 1/3 and 2/3
        third_length = length / 3
        p_third = (x1 + unit_x * third_length, y1 + unit_y * third_length)
        p_two_thirds = (x1 + unit_x * 2 * third_length, y1 + unit_y * 2 * third_length)
        
        # Height of the equilateral triangle peak
        triangle_height = third_length * math.sqrt(3) / 2
        
        # Peak point (middle of the transformed segment)
        mid_x = (p_third[0] + p_two_thirds[0]) / 2
        mid_y = (p_third[1] + p_two_thirds[1]) / 2
        peak = (mid_x + perp_x * triangle_height, mid_y + perp_y * triangle_height)
        
        # Return the arrowhead pattern: start -> 1/3 -> peak -> 2/3 -> end
        return [p1, p_third, peak, p_two_thirds, p2]
    
    def generate_arrowhead(self, depth):
        """Generate Sierpinski arrowhead curve with given recursion depth"""
        # Start with initial line segment
        points = self.get_initial_line()
        
        # Apply arrowhead transformation for each depth level
        for _ in range(depth):
            new_points = []
            for i in range(len(points) - 1):
                current_point = points[i]
                next_point = points[i + 1]
                
                # Apply arrowhead transformation to this segment
                transformed = self.apply_arrowhead_transformation(current_point, next_point)
                
                # Add all but the last point (to avoid duplication)
                new_points.extend(transformed[:-1])
            
            # Add the final point
            if points:
                new_points.append(points[-1])
                
            points = new_points
            
        return points
    
    def save_image(self, points, filename):
        """Save the arrowhead curve as an image"""
        # Create a white image
        image = Image.new('RGB', (self.size, self.size), 'white')
        draw = ImageDraw.Draw(image)
        
        # Convert points to integers for drawing
        int_points = [(int(x), int(y)) for x, y in points]
        
        # Draw the arrowhead curve as connected lines
        if len(int_points) > 1:
            # Draw lines connecting each point to the next
            for i in range(len(int_points) - 1):
                start_point = int_points[i]
                end_point = int_points[i + 1]
                draw.line([start_point, end_point], fill='black', width=2)
        
        # Save the image
        image.save(filename)