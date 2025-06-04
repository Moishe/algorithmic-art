# ABOUTME: Main CLI interface for generative computer art algorithms
# ABOUTME: Handles command line argument parsing and coordinates art generation

import click
from koch_snowflake import KochSnowflake
from sierpinski_gasket import SierpinskiGasket
from sierpinski_arrowhead import SierpinskiArrowhead
from mandelbrot_set import MandelbrotSet


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    """Generate procedural computer art using various algorithms.
    
    Available algorithms:
    - koch-snowflake: Generate Koch snowflake fractal using --recursion-depth
    - sierpinski-gasket: Generate Sierpinski gasket fractal using --recursion-depth  
    - sierpinski-arrowhead: Generate Sierpinski arrowhead fractal using --recursion-depth
    - mandelbrot-set: Generate Mandelbrot set fractal using --num-iterations
    
    Use --help with any subcommand to see algorithm-specific options.
    """
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


@main.command("koch-snowflake")
@click.option('--recursion-depth', type=int, required=True, help='Recursion depth for fractal generation')
@click.option('--size', type=int, required=True, help='Width and height of output image')
@click.option('--output', required=True, help='Output filename')
def koch_snowflake(recursion_depth, size, output):
    """Generate Koch snowflake fractal."""
    koch = KochSnowflake(size=size)
    points = koch.generate_snowflake(depth=recursion_depth)
    koch.save_image(points, output)


@main.command("sierpinski-gasket")
@click.option('--recursion-depth', type=int, required=True, help='Recursion depth for fractal generation')
@click.option('--size', type=int, required=True, help='Width and height of output image')
@click.option('--output', required=True, help='Output filename')
def sierpinski_gasket(recursion_depth, size, output):
    """Generate Sierpinski gasket fractal."""
    gasket = SierpinskiGasket(size=size)
    triangles = gasket.generate_gasket(depth=recursion_depth)
    gasket.save_image(triangles, output)


@main.command("sierpinski-arrowhead")
@click.option('--recursion-depth', type=int, required=True, help='Recursion depth for fractal generation')
@click.option('--size', type=int, required=True, help='Width and height of output image')
@click.option('--output', required=True, help='Output filename')
def sierpinski_arrowhead(recursion_depth, size, output):
    """Generate Sierpinski arrowhead fractal."""
    arrowhead = SierpinskiArrowhead(size=size)
    points = arrowhead.generate_arrowhead(depth=recursion_depth)
    arrowhead.save_image(points, output)


@main.command("mandelbrot-set")
@click.option('--num-iterations', type=int, required=True, help='Maximum number of iterations for convergence testing')
@click.option('--size', type=int, required=True, help='Width and height of output image')
@click.option('--output', required=True, help='Output filename')
def mandelbrot_set(num_iterations, size, output):
    """Generate Mandelbrot set fractal."""
    mandelbrot = MandelbrotSet(size=size, max_iterations=num_iterations)
    mandelbrot_data = mandelbrot.generate_mandelbrot_set()
    mandelbrot.save_image(mandelbrot_data, output)


if __name__ == "__main__":
    main()
