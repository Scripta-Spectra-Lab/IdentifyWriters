from setuptools import setup

setup(
    name="IdentWriters", 
    version="0.1.0",  # Replace with your package version
    description="A versatile package for handling text documents and performing various statistical tests to identify the number of writers who contributed to the document",  # Brief description of the package
    long_description=open('README.md').read(),
    author="Yishai Shor & Dr. Barak Sober",  
    author_email="yishai.shor@gmail.com",  
    url="https://github.com/Yishai-Shor/Using-Statistical-Methods-to-Identify-Number-of-Writers-in-the-Dead-Sea-Scrolls",  
    packages=['IdentWriters'], 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
