# ABOUTME: Implementation of the Mandelbrot set fractal algorithm
# ABOUTME: Generates Mandelbrot set visualizations through complex number iteration

import math
from PIL import Image, ImageDraw


class MandelbrotSet:
    def __init__(self, size, center_real=-0.5, center_imag=0, zoom=1.0, max_iterations=100):
        self.size = size
        self.center_real = center_real
        self.center_imag = center_imag
        self.zoom = zoom
        self.max_iterations = max_iterations
        
        # Define the complex plane bounds
        self.range = 2.0 / zoom  # Base range is 4 units (-2 to 2), scaled by zoom
        
    def pixel_to_complex(self, x, y):
        """Convert pixel coordinates to complex plane coordinates"""
        # Map pixel coordinates to complex plane
        real = self.center_real + (x - self.size / 2) * self.range / self.size
        imag = self.center_imag - (y - self.size / 2) * self.range / self.size  # Flip y-axis
        return real, imag
    
    def mandelbrot_iteration(self, real, imag):
        """Calculate the number of iterations for a point to diverge"""
        c_real, c_imag = real, imag
        z_real, z_imag = 0, 0
        
        for iteration in range(self.max_iterations):
            # Calculate z^2 + c
            z_real_new = z_real * z_real - z_imag * z_imag + c_real
            z_imag_new = 2 * z_real * z_imag + c_imag
            
            z_real, z_imag = z_real_new, z_imag_new
            
            # Check if the point has diverged (magnitude > 2)
            if z_real * z_real + z_imag * z_imag > 4:
                return iteration
                
        return self.max_iterations
    
    def generate_mandelbrot_set(self):
        """Generate the Mandelbrot set data as a 2D matrix"""
        mandelbrot_data = []
        
        for y in range(self.size):
            row = []
            for x in range(self.size):
                real, imag = self.pixel_to_complex(x, y)
                iterations = self.mandelbrot_iteration(real, imag)
                row.append(iterations)
            mandelbrot_data.append(row)
            
        return mandelbrot_data
    
    def save_image(self, mandelbrot_data, filename):
        """Save the Mandelbrot set as an image"""
        # Create a new image
        image = Image.new('RGB', (self.size, self.size), 'white')
        draw = ImageDraw.Draw(image)
        
        # Color the pixels based on iteration count
        for y in range(self.size):
            for x in range(self.size):
                iterations = mandelbrot_data[y][x]
                
                if iterations == self.max_iterations:
                    # Points in the set are black
                    color = (0, 0, 0)
                else:
                    # Points outside the set are colored based on iteration count
                    # Create a gradient from blue to red
                    ratio = iterations / self.max_iterations
                    red = int(255 * ratio)
                    blue = int(255 * (1 - ratio))
                    green = int(128 * ratio)
                    color = (red, green, blue)
                
                image.putpixel((x, y), color)
        
        # Save the image
        image.save(filename)