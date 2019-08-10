from setuptools import setup, find_packages

setup(
    name="infinity",
    version="0.1",
    author="Naren Thiagarajan",
    author_email="narenst@gmail.com",
    url="https://www.floydhub.com",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "click",
        "requests",
        "pytz",
        "tabulate",
        "PyYAML",
        "boto3>=1.0.0"
    ],
    setup_requires=[
        "flake8",
    ],
    dependency_links=[],
    entry_points={
        "console_scripts": [
            "infinity = infinity.main:cli",
        ],
    },
    tests_require=[
        "pytest",
        "mock>=1.0.1",
    ],
)