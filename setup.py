from setuptools import setup, find_packages

setup(
    name="booklover",  # Name of the package
    version="0.1",
    packages=find_packages(where="src"),  # Automatically find packages inside src/
    package_dir={"": "src"},  # Indicate the location of the package
    test_suite='tests',  # Point to the test suite
    install_requires=[],  # Add any dependencies here if needed
    entry_points={
        'console_scripts': [],
    },
)
