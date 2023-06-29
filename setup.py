import setuptools

setuptools.setup(
    name="NSEDownload",
    version="5.0.1",
    author="Jinit",
    description="Download Stocks data from NSE",

    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['beautifulsoup4', 'requests', 'pandas', 'numpy', 'timedelta', 'fuzzywuzzy']
)
