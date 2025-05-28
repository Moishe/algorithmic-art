# ABOUTME: Implementation of the Sierpinski arrowhead fractal using L-systems
# ABOUTME: Generates arrowhead curve fractals via string rewriting and turtle graphics

import math
from PIL import Image, ImageDraw


class SierpinskiArrowhead:
    def __init__(self, size, step_length=None):
        self.size = size
        self.step_length = step_length or 10  # Fixed step length for initial generation
        self.angle = 60  # degrees
        
    def generate_lsystem_string(self, depth):
        """Generate L-system string using Sierpinski arrowhead rules"""
        # Axiom: A
        # Rules: A -> B-A-B, B -> A+B+A
        current = "A"
        
        for _ in range(depth):
            next_string = ""
            for char in current:
                if char == "A":
                    next_string += "B-A-B"
                elif char == "B":
                    next_string += "A+B+A"
                else:
                    next_string += char
            current = next_string
            
        return current
    
    def interpret_turtle_commands(self, lsystem_string, start_pos=None, start_angle=0):
        """Interpret L-system string as turtle graphics commands"""
        if start_pos is None:
            start_pos = (self.size * 0.2, self.size * 0.8)
            
        points = []
        x, y = start_pos
        angle = start_angle  # degrees
        
        points.append((x, y))
        
        for char in lsystem_string:
            if char in ["A", "B"]:  # Both A and B mean "move forward"
                # Convert angle to radians and calculate new position
                rad = math.radians(angle)
                new_x = x + self.step_length * math.cos(rad)
                new_y = y + self.step_length * math.sin(rad)
                x, y = new_x, new_y
                points.append((x, y))
            elif char == "+":  # Turn left
                angle += self.angle
            elif char == "-":  # Turn right
                angle -= self.angle
                
        return points
    
    def generate_arrowhead(self, depth):
        """Generate Sierpinski arrowhead curve with given recursion depth"""
        # Generate L-system string
        lsystem_string = self.generate_lsystem_string(depth)
        
        # Convert to points using turtle graphics with temporary step length
        temp_points = self.interpret_turtle_commands(lsystem_string)
        
        # Scale and center the curve to fit the image
        scaled_points = self.scale_to_fit(temp_points)
        
        return scaled_points
    
    def scale_to_fit(self, points):
        """Scale and center the curve to fit within the image bounds"""
        if len(points) < 2:
            return points
            
        # Calculate bounding box
        xs = [p[0] for p in points]
        ys = [p[1] for p in points]
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)
        
        # Current dimensions
        current_width = max_x - min_x
        current_height = max_y - min_y
        
        if current_width == 0 or current_height == 0:
            return points
            
        # Target dimensions (with some margin)
        margin = self.size * 0.1  # 10% margin
        target_width = self.size - 2 * margin
        target_height = self.size - 2 * margin
        
        # Calculate scale factor (use the smaller ratio to maintain aspect ratio)
        scale_x = target_width / current_width
        scale_y = target_height / current_height
        scale = min(scale_x, scale_y)
        
        # Scale and translate points
        scaled_points = []
        for x, y in points:
            # Translate to origin
            x_norm = x - min_x
            y_norm = y - min_y
            
            # Scale
            x_scaled = x_norm * scale
            y_scaled = y_norm * scale
            
            # Center in image
            final_width = current_width * scale
            final_height = current_height * scale
            x_final = x_scaled + (self.size - final_width) / 2
            y_final = y_scaled + (self.size - final_height) / 2
            
            scaled_points.append((x_final, y_final))
            
        return scaled_points
    
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