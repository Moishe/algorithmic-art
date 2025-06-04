# Generative Computer Art

This project is a generative/procedural computer art explorer that creates fractal visualizations using various mathematical algorithms.

## Usage

The application uses algorithm-specific subcommands. Get help for any command:

```bash
uv run main.py --help
uv run main.py [algorithm] --help
```

## Supported Algorithms

### Koch Snowflake
```bash
uv run main.py koch-snowflake --recursion-depth <n> --size <pixels> --output <filename>
```

### Sierpinski Gasket  
```bash
uv run main.py sierpinski-gasket --recursion-depth <n> --size <pixels> --output <filename>
```

### Sierpinski Arrowhead
```bash
uv run main.py sierpinski-arrowhead --recursion-depth <n> --size <pixels> --output <filename>
```

### Mandelbrot Set
```bash
uv run main.py mandelbrot-set --num-iterations <n> --size <pixels> --output <filename>
```

## Parameters

- `--recursion-depth`: Depth of recursion for fractal algorithms (koch-snowflake, sierpinski-gasket, sierpinski-arrowhead)
- `--num-iterations`: Maximum iterations for convergence testing (mandelbrot-set)
- `--size`: Width and height of output image in pixels
- `--output`: Output filename for the generated image

## Development

Run tests with:
```bash
uv run pytest
```
