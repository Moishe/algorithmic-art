This project is a generative/procedural computer art explorer.

Create AI art by calling main.py like this:

`uv run main.py [algorithm_name] --detail-level <n> --size <h> --output <filename.jpg>`

algorithm_name specifies the algorithm. Currently supported algorithms are:
- koch-snowflake: Generates a Koch snowflake fractal
- sierpinski-gasket: Generates a Sierpinski gasket fractal
detail-level is the level of detail. For recursive algorithms like the koch snowflake, this is the depth of recursion. For iterative algorithms like Mandelbrot (not yet supported) this is the number of iterations. For cellular automata, this is the number of generations to run.
size specifies the width and height of the resulting jpg.
output is the output filename.
