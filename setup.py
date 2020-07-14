import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hypothesis-grammars",
    version="0.1.0",
    author="Sergey Bronnikov",
    author_email="estetus@gmail.com",
    description="Lark grammars for using wht Hypothesis testing library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ligurio/hypothesis-grammars",
    packages=setuptools.find_packages(),
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Testing",
    ],
    python_requires='>=3.6',
)
