import sys
import subprocess


required_packages = ["Pillow==7.2.0", "PyMySQL==0.10.0",
                     "SQLAlchemy==1.3.19", "loguru==0.5.2",
                     "matplotlib==3.3.1", "numpy==1.19.1",
                     "orca==1.5.3", "pandas==1.1.1",
                     "plotly==4.9.0", "requests==2.24.0",
                     "scikit-learn==0.23.2", "scipy==1.5.2",
                     "seaborn==0.10.1"]

# implement pip as a subprocess:
try:
    for pkg in required_packages:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', pkg])

    # process output with an API in the subprocess module:
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

    print(installed_packages)

except Exception as e:
    print(e)


