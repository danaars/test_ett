from setuptools import setup, find_packages

setup(
    name = "GiTall",
    version = "3.6",
    packages = find_packages(),
    install_requires = [
        'pip @ git+https://github.com/danaars/test_ett.git#subdirectory=submodule'
    ]
)
