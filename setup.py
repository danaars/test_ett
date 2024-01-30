from setuptools import setup, find_packages

setup(
    name = "GiTall",
    version = "3.4",
    packages = find_packages(),
    install_requires = [
        'gitall @ https://github.com/danaars/test_ett.git#subdirectory=submodule'
    ]
)
