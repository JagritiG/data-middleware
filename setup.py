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
    version="0.0.9",
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
    # install_requires=["Pillow==7.2.0", "PyMySQL==0.10.0",
    #                   "SQLAlchemy==1.3.19", "loguru==0.5.2",
    #                   "matplotlib==3.3.2", "numpy==1.19.1",
    #                   "orca==1.5.3", "pandas==1.1.1",
    #                   "plotly==4.9.0", "requests==2.24.0",
    #                   "scikit-learn==0.23.2", "scipy==1.5.2",
    #                   "seaborn==0.10.1", "click==7.1.2"],
    install_requires=["Pillow==7.2.0",
                      "PyMySQL==0.10.1",
                      "Pygments==2.7.1",
                      "SQLAlchemy==1.3.19",
                      "argparse==1.4.0",
                      "bleach==3.2.1",
                      "blessings==1.7",
                      "certifi==2020.6.20",
                      "chardet==3.0.4",
                      "checkmyreqs==0.3.1",
                      "click==7.1.2",
                      "colorama==0.4.3",
                      "conda==4.3.16",
                      "cycler==0.10.0",
                      "docutils==0.16",
                      "executing==0.5.2",
                      "idna==2.10",
                      "importlib-metadata==2.0.0",
                      "joblib==0.16.0",
                      "keyring==21.4.0",
                      "kiwisolver==1.2.0",
                      "linecache2==1.0.0",
                      "loguru==0.5.3",
                      "matplotlib==3.3.2",
                      "matplotlylib==0.1.0",
                      "mysql==0.0.2",
                      "mysqlclient==2.0.1",
                      "numexpr==2.7.1",
                      "numpy==1.19.2",
                      "orca==1.5.3",
                      "packaging==20.4",
                      "panda==0.3.1",
                      "pandas==1.1.2",
                      "pip==20.2.3",
                      "pkginfo==1.5.0.1",
                      "plotly==4.10.0",
                      "psutil==5.7.2",
                      "pycosat==0.6.3",
                      "pyparsing==3.0.0a2",
                      "python-dateutil==2.8.1",
                      "pytz==2020.1",
                      "readme-renderer==26.0",
                      "requests==2.24.0",
                      "requests-toolbelt==0.9.1",
                      "retrying==1.3.3",
                      "rfc3986==1.4.0",
                      "ruamel.yaml==0.16.12",
                      "ruamel.yaml.clib==0.2.2",
                      "scikit-learn==0.23.2",
                      "scipy==1.5.2",
                      "seaborn==0.11.0",
                      "setuptools==50.3.0",
                      "six==1.15.0",
                      "tables==3.6.1",
                      "threadpoolctl==2.1.0",
                      "toolz==0.11.1",
                      "tqdm==4.50.0",
                      "traceback2==1.4.0",
                      "twine==3.2.0",
                      "urllib3==1.25.10",
                      "varname==0.4.0",
                      "webencodings==0.5.1",
                      "wheel==0.35.1",
                      "zipp==3.2.0"],
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
