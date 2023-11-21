# Matrix-Matrix Multiplication

## Overview

This Python implementation uses Flask to create a web-based simulation for matrix-matrix multiplication using a linear array. The simulation visualizes the computation steps involved in multiplying two matrices, `matrix1` and `matrix2`, and displays intermediate values during each step. The linear array includes delay elements to illustrate the flow of data through the system.

## Prerequisites

Before running the program, ensure that you have Python and Flask installed. You can install Flask using the following command:

```bash
pip install Flask
```

## How to Run

1. Run the Flask application:

```bash
python app.py
```

2. Open your web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to interact with the matrix-multiplication simulation.

## Detailed Logic

### 1. Matrix Initialization and Transformation

- Two matrices, `matrix1` and `matrix2`, are initialized in the Python code.
- The `transpose` function is used to transpose matrices as needed for the linear array computation.
- The `add_delays` function adds delay elements to the matrices to simulate a linear array with delays.

### 2. Web Interface

- The Flask application has two routes: `'/'` and `'/next_step'`.
- The `'/'` route renders the initial state of the matrices and linear array on the web page.
- The `'/next_step'` route advances the simulation by one step and updates the web page with the new state.

### 3. Linear Array Computation

- The linear array computation is simulated using a 2D array of cells (`cells`).
- Each cell in the array contains:
  - `c`: The result of the multiplication.
  - `m1_in`, `m1_out`: Input and output values from `matrix1`.
  - `m2_in`, `m2_out`: Input and output values from `matrix2`.

### 4. Matrix Propagation and Computation

- The `'next_step'` route propagates input values through the linear array.
- For each cell, the input values (`m1_in` and `m2_in`) are calculated based on the previous cell's output.
- The algorithm updates the cell's state, including the result of the multiplication (`c`).

### 5. Web Page Display

- The HTML template (`index.html`) uses Jinja2 templating to display the matrix values and cell states.
- The template includes a grid that represents the linear array and updates dynamically with each step.
- CSS styles (`style.css`) enhance the visual representation of the matrices and linear array.

## Acknowledgments

This simulation serves as an educational tool for understanding the steps involved in matrix-matrix multiplication using a linear array. It provides a visual representation of the computation process and can be used for learning purposes or as a reference for implementing similar simulations.


![First page](https://github.com/IuliaVrabie/Matrix-Matrix-Multiplication/blob/668d8e317ddf1ca1e421eb0e44b87d7f63dc5aa2/mmm.png)
