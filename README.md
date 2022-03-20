# Relart

Relart is a Python package that contains handy functions for every day data science work. 

## Installation and updating
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Toolbox like below. 
Rerun this command to check for and install  updates .
```bash
pip install git+https://github.com/artemmoskalev/relart
```

## Usage
Features:
* relart.cross_validation --> contains modules to help with the model selection
* relart.feature_engineering --> contains modules for creating/modifying existing features
* relart.modelling --> has various models not available elsewhere

#### Demo of some of the features:
```python
from relart import cross_validation as cv

grid = cv.cv_grid(alpha=[0.1, 0.2], reg_lambda=[1, 10], model=["Poisson", "Negative Binomial"])
print(grid)

```

## Contributing
For major changes, please open an issue first to discuss what you would like to change. Then, a pull request.