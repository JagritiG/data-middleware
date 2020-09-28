import sys
import subprocess
import conda.cli.python_api as Conda

required_packages = ["Pillow==7.2.0", "PyMySQL==0.10.0",
                     "SQLAlchemy==1.3.19", "loguru==0.5.2",
                     "matplotlib==3.3.1", "numpy==1.19.1",
                     "orca==1.5.3", "pandas==1.1.1",
                     "plotly==4.9.0", "requests==2.24.0",
                     "scikit-learn==0.23.2", "scipy==1.5.2",
                     "seaborn==0.10.1", "setuptools==39.1.0"]

# implement conda as a subprocess:
try:
    for pkg in required_packages:
        subprocess.check_call([sys.executable, '-m', 'conda', 'install', pkg])
except Exception as e:
    print(e)

