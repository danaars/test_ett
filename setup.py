from setuptools import setup, find_packages

setup(
    name = "GiTall",
    version = "3.5",
    packages = find_packages(),
    install_requires = [
        'pip @ https://github.com/danaars/test_ett.git#subdirectory=submodule'
    ]
)
