"""
setup.py serves two primary functions:
It’s the file where various aspects of your project are configured.
The primary feature of setup.py is that it contains a global setup() function.
The keyword arguments to this function are how specific details of your project are defined.
It’s the command line interface for running various commands that relate to packaging tasks.
To get a listing of available commands, run python setup.py --help-commands.
"""
import setuptools
from os import path

here = path.abspath(path.dirname(__file__))

setuptools.setup(
    name="datamidware",
    version="0.0.2",
    description="Data Middleware",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",

    # Author details
    author="Jagriti Goswami",
    author_email="jagritigoswami84@gmail.com",


    # The project's main homepage.
    url="https://github.com/JagritiG/dataware",

    # Choose your license
    license='MIT',

    packages=setuptools.find_packages(),
    install_requires=["Pillow==7.2.0", "PyMySQL==0.10.0",
                      "SQLAlchemy==1.3.19", "loguru==0.5.2",
                      "matplotlib==3.3.1", "numpy==1.19.1",
                      "orca==1.5.3", "pandas==1.1.1",
                      "plotly==4.9.0", "requests==2.24.0",
                      "scikit-learn==0.23.2", "scipy==1.5.2",
                      "seaborn==0.10.1", "click==7.1.2"],
    classifiers=[
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",

        # Pick your license as you wish (should match "license" above)
        "License :: OSI Approved :: MIT License",

        # Specify the Python versions you support here.
        "Programming Language :: Python :: 3.7",
    ],
    include_package_data=True,
)
