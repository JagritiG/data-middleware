import sys
import subprocess

# implement pip as a subprocess:
try:
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

    found = False
    for pkg in installed_packages:
        if pkg == "checkmyreqs":
            found = True
            print("Package already installed!")
            break
    if not found:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', "checkmyreqs"])

    print(subprocess.run(["checkmyreqs", "-f", "path/requirements.txt", "-p", "3.7"]))

except Exception as e:
    print(e)



