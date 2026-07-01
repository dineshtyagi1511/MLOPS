from setuptools import setup, find_packages

# Read requirements.txt
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="MLOPS",
    version="1.0.0",
    author="Dinesh Tyagi",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.10",
)