import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NSEDownload",
    version="0.1.1",
    author="Jinit S",
    description="Download Stocks and Indices Data from NSE",
    long_description=long_description,
    long_description_content_type="text/markdown",
  
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # python_requires='>=3.6',
)
