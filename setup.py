from setuptools import setup, find_packages

setup(
    name="sweetgreen",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "sweetgreen-cli = sweetgreen.cli:main"
        ]
    },
    install_requires=[
        "alabaster==1.0.0",
        "babel==2.16.0",
        "certifi==2024.8.30",
        "charset-normalizer==3.4.0",
        "docutils==0.21.2",
        "idna==3.10",
        "imagesize==1.4.1",
        "iniconfig==2.0.0",
        "Jinja2==3.1.4",
        "joblib==1.4.2",
        "MarkupSafe==3.0.2",
        "networkx==3.4.1",
        "numpy==2.1.2",
        "packaging==24.1",
        "pandas==2.2.3",
        "pluggy==1.5.0",
        "Pygments==2.18.0",
        "pytest==8.3.3",
        "python-dateutil==2.9.0.post0",
        "pytz==2024.2",
        "requests==2.32.3",
        "scikit-learn==1.5.2",
        "scipy==1.14.1",
        "six==1.16.0",
        "snowballstemmer==2.2.0",
        "Sphinx==8.1.3",
        "sphinxcontrib-applehelp==2.0.0",
        "sphinxcontrib-devhelp==2.0.0",
        "sphinxcontrib-htmlhelp==2.1.0",
        "sphinxcontrib-jsmath==1.0.1",
        "sphinxcontrib-qthelp==2.0.0",
        "sphinxcontrib-serializinghtml==2.0.0",
        "threadpoolctl==3.5.0",
        "tzdata==2024.2",
        "urllib3==2.2.3",
        "bitarray==2.3.4"
    ],
    python_requires=">=3.7",
    author="Isfar Baset, Bella Shi, Sheeba Moghal, Jacky Zhang, Ziyan Di",
    description="A package for Bloom Filter and LSH experiments",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/DSAN6700-24Fall/assignment-2-sweetgreen.git"
)
