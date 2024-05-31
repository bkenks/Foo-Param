
# Foo-Param

A python package created for the hypothetical Foo et al. parameterization. The purpose is to illustrate my ability to create a python package at an enterprise level with collaboration and expansion in mind.
## Installation

Install package with pip. (Preferable in Python Virtual Environment)

```bash
  pip install /Foo-Param
```
    
## Usage/Examples

This is example code to start using this package.
```python
from foo_param.calculation import calculate_volume

RADIUS = 5
VOLUME = calculate_volume(RADIUS)
print(f"The radius of a sphere with a radius of {RADIUS} is {VOLUME:0.3F}")
```


## Running Tests

To run tests, run the following command from within the Foo-Param directory.

```bash
  python -m unittest discover tests
```


## Contact

- Brian Kenkel - [![LinkedIn][linkedin-shield]](https://linkedin.com/in/briankenkel) - briankenkel.t@gmail.com

[linkedin-shield]: https://img.shields.io/badge/LinkedIn-l?style=for-the-badge&logo=linkedin&logoColor=FFFFFF&color=0A66C2
