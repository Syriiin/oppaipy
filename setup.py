import setuptools

with open("README.md", "r") as fp:
    long_description = fp.read()

setuptools.setup(
    name="oppaipy",
    version="1.0.1",
    author="Syrin",
    author_email="syrin@syrin.me",
    description="A simple object-oriented python3 wrapper around the python bindings of oppai-ng",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Syriiin/oppaipy",
    packages=setuptools.find_packages(),
    install_requires=[
        "oppai==3.2.1"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)
