# Option Pricing Trees in Python

A high-performance, vectorized Python implementation for pricing European, American, and Barrier options using binomial trees and NumPy. 

## 📁 Project Structure

```text
├── src/
│   ├── forward_tree.py    # Generates the underlying asset price lattice
│   └── backwards_tree.py  # Evaluates option values, early exercises, and barriers
├──setup.py                # Creates files and directories
├── main.py                # Execution script for running simulations
└── README.md

## 🚀 Features

* **European Options:** Standard standard-path pricing.
* **American Options:** Handles early-exercise features seamlessly.
* **Barrier Options:** Supports Up-and-In, Up-and-Out, Down-and-In, and Down-and-Out structures using efficient NumPy matrix masking and slicing.
* **Vectorized Performance:** Leverages NumPy arrays and matrix operations to avoid slow, explicit Python loops.

## 🛠️ Prerequisites

Make sure you have Python and NumPy installed:

```bash
pip install numpy
