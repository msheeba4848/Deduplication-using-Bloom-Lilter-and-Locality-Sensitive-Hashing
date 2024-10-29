from setuptools import setup, find_packages

setup(
    name="yourpackage",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "yourpackage-cli = yourpackage.cli:main"
        ]
    },
    install_requires=[
        # Add any dependencies required for your package here, e.g.:
        # 'numpy', 'scipy'
    ],
    python_requires=">=3.7",
    author="Your Name",
    author_email="your.email@example.com",
    description="A package for Bloom Filter and LSH experiments",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/yourpackage",  # Update with your repository URL if applicable
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
