# ABOUTME: Main CLI interface for generative computer art algorithms
# ABOUTME: Handles command line argument parsing and coordinates art generation

import click
import sys
from koch_snowflake import KochSnowflake


@click.command()
@click.argument('algorithm_name')
@click.option('--detail-level', type=int, required=True, help='Level of detail/recursion depth')
@click.option('--size', type=int, required=True, help='Width and height of output image')
@click.option('--output', required=True, help='Output filename')
def main(algorithm_name, detail_level, size, output):
    """Generate procedural computer art using various algorithms."""
    
    if algorithm_name == "koch-snowflake":
        koch = KochSnowflake(size=size)
        points = koch.generate_snowflake(depth=detail_level)
        koch.save_image(points, output)
    else:
        click.echo(f"Error: Unknown algorithm '{algorithm_name}'", err=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
