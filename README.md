# Polynomial Interpolation Calculator

## Overview

This Python project is a command-line tool that calculates the polynomial that passes through a set of points provided by the user. The script constructs a Vandermonde matrix based on the input points and uses Cramer's rule to solve for the polynomial coefficients. It then displays the resulting polynomial in a readable format.

## Features

- **Polynomial Calculation**: Given a set of points, the script calculates the unique polynomial that passes through all of them.
- **Interactive User Input**: The user is prompted to enter the coordinates of the points, and the program interactively calculates and displays the polynomial.
- **Determinant Calculation**: The script uses the determinant of the matrix to calculate the polynomial coefficients, ensuring accurate results.
- **Error Handling**: The script includes basic error handling to ensure that inputs are valid and matrices are not singular.

## Requirements

- Python 3.x
- NumPy library

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/3ina/Polynomial-interpolation.git
    cd polynomial-interpolation
    ```

2. **Install dependencies**:
    Make sure you have Python 3 and pip installed. Then, install the required Python packages:
    ```sh
    pip install numpy
    ```



## Usage

To run the script, simply execute the Python file:

```sh
python main.py
