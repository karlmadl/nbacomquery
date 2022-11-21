from setuptools import setup, find_packages

VERSION = "0.0.13"
DESCRIPTION = "nba.com/stats querying package"
LONG_DESCRIPTION = "nba.com/stats querying package and more information"

setup(
    name="nbacomquery", 
    version=VERSION,
    author="Karl Madl",
    author_email="<karl_madl@yahoo.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    license="MIT",
    packages=find_packages(),
    package_data={'nbacomquery': ['config/*.yaml']},
    install_requires=["pandas", "pyyaml"],     
    keywords=["python", "nba", "stats"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English"
    ]
)