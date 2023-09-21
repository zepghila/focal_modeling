# Simple Focal Length Modeling for Tuneable Lenses Characterisation System

## Background

This repository contains a Python script designed to aid in the experimental setup for measuring the effective focal distance (EFD) of tuneable lenses. The script models the combined focal length of a system comprising a lens with a known focal length and a tuneable lens whose focal length varies.

The primary objective for this script is to determine the EFD of a tuneable lens, which has an infinite focus at rest and reduces its focal length upon applying a voltage. By adding a lens with a known focal length to the system, the EFD of the tuneable lens can be calculated.

The concept follows from the experimental setup described in the paper ["Smart Lenses with Electrically Tuneable Astigmatism"](https://www.nature.com/articles/s41598-019-52168-8). The EFD-measurement setup used in the paper can be found in the supplementary information [here](https://static-content.springer.com/esm/art%3A10.1038%2Fs41598-019-52168-8/MediaObjects/41598_2019_52168_MOESM1_ESM.pdf).

## Description

The script models the combined focal length of two lenses placed in series. The formula used to calculate the combined focal length of two lenses separated by a distance \( d \) is derived from the principle of lens combinations:

$$
\frac{1}{f_{combined}} = \frac{1}{f_1} + \frac{1}{f_2} - \frac{d}{f_1 \times f_2}
$$

Where:
- `f_1` is the focal length of the first lens.
- `f_2` is the focal length of the second lens.
- `d` is the distance between the two lenses.


## Features

- **3D Plotting**: Visualize the relationship between the EFD of the tunable lens, the known focal length, and the measured EFD at the output.
- **2D Slice Plotting**: View a 2D slice of the 3D plot for a specific known focal length.

## Requirements

- Python 3.x
- NumPy
- Matplotlib

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/yourusername/focal_modeling.git
    ```

2. Navigate to the cloned directory:

3. Install the required packages using pipenv:
    ```
    pipenv install
    ```


## Usage

Activate the virtual environment:

```
pipenv shell
```


Run the `main.py` script to generate the plots:

```
python main.py
```

