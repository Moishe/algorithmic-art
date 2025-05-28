# ABOUTME: Implementation of the Sierpinski Gasket fractal algorithm
# ABOUTME: Generates triangle subdivision fractals and renders them to image files

import math
from PIL import Image, ImageDraw


class SierpinskiGasket:
    def __init__(self, size):
        self.size = size
        
    def get_initial_triangle(self):
        """Generate an equilateral triangle as the base for the Sierpinski Gasket"""
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
    
    def subdivide_triangle(self, triangle):
        """Subdivide a triangle into 3 corner triangles for Sierpinski Gasket"""
        p1, p2, p3 = triangle
        
        # Calculate midpoints of each edge
        mid12 = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
        mid23 = ((p2[0] + p3[0]) / 2, (p2[1] + p3[1]) / 2)
        mid31 = ((p3[0] + p1[0]) / 2, (p3[1] + p1[1]) / 2)
        
        # Create 3 corner triangles
        corner1 = [p1, mid12, mid31]
        corner2 = [p2, mid23, mid12]
        corner3 = [p3, mid31, mid23]
        
        return [corner1, corner2, corner3]
    
    def generate_gasket(self, depth):
        """Generate Sierpinski Gasket triangles with given recursion depth"""
        # Start with initial triangle
        triangles = [self.get_initial_triangle()]
        
        # Apply subdivision for each depth level
        for _ in range(depth):
            new_triangles = []
            for triangle in triangles:
                subdivided = self.subdivide_triangle(triangle)
                new_triangles.extend(subdivided)
            triangles = new_triangles
            
        return triangles
    
    def save_image(self, triangles, filename):
        """Save the gasket triangles as an image"""
        # Create a white image
        image = Image.new('RGB', (self.size, self.size), 'white')
        draw = ImageDraw.Draw(image)
        
        # Draw each triangle
        for triangle in triangles:
            # Convert points to integers for drawing
            int_points = [(int(x), int(y)) for x, y in triangle]
            
            # Draw the triangle outline
            if len(int_points) == 3:
                # Draw lines connecting each point to form triangle
                for i in range(3):
                    start_point = int_points[i]
                    end_point = int_points[(i + 1) % 3]
                    draw.line([start_point, end_point], fill='black', width=1)
        
        # Save the image
        image.save(filename)