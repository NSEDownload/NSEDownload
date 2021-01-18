import setuptools

setuptools.setup(
    name="NSEDownload",
    version="3.0.0",
    author="Jinit S",
    description="Download Stocks and Indices Data from NSE",
  
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = ['beautifulsoup4', 'requests', 'numpy', 'pandas', 'timedelta','fuzzywuzzy'],
)