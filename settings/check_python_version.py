# Python version compatibility check
import sys

try:
    if not sys.version_info.major == 3 and sys.version_info.minor >= 7:
        print("Python 3.7 or higher is required.")
        print("You are using Python {}.{}.".format(sys.version_info.major, sys.version_info.minor))

    else:
        print("You are using Python {}.{}.".format(sys.version_info.major, sys.version_info.minor))
        print("Required python version is already installed")


except Exception as e:
    print(e)

finally:
    sys.exit(1)


