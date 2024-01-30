from setuptools import setup, find_packages

setup(
    name = "GiTall",
    version = "3.3",
    packages = find_packages(),
    install_requires = [
        'https://github.com/danaars/test_ett.git#subdirectory=submodule'
    ]
)
