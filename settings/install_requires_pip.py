import sys
import subprocess


# implement pip as a subprocess:
try:
    required_packages = []
    with open("requirements.txt", "r") as f:
        for line in f:
            required_packages.append(line)
            print(line)

    print(required_packages[0])

    for pkg in required_packages:
        subprocess.run([sys.executable, '-m', 'pip', 'install', pkg], stdout=True)

except Exception as e:
    print(e)


