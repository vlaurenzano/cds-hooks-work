import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cds-hooks-work",  # Replace with your own username
    version="0.0.1",
    author="vlaurenzano",
    author_email="vincent.laurenzano@gmail.com",
    description="A framework for implementing cds hooks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vlaurenzano/cds-hooks-work",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
