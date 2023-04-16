import setuptools

setuptools.setup(
    name="NSEDownload",
    version="4.1.2",
    author="Jinit S",
    description="Download Stocks and Indices Data from NSE",

    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['beautifulsoup4', 'requests', 
                      'pandas', 'numpy','timedelta', 'fuzzywuzzy'],
)
