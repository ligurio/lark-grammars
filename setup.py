import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lark-grammars",
    version="0.1.0",
    author="Sergey Bronnikov",
    author_email="estetus@gmail.com",
    description="Lark grammars for using wht Hypothesis testing library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={'lark_grammars': 'lark_grammars'},
    package_data={'lark_grammars': ['grammars/*.lark']},
    url="https://github.com/ligurio/lark-grammars",
    packages=setuptools.find_packages(),
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Testing",
    ],
    python_requires='>=3.6',
    install_requires=[
        'hypothesis',
        'lark-parser'],
    project_urls={
        'Bug Reports': 'https://github.com/ligurio/lark-grammars/issues',
        'Source': 'https://github.com/ligurio/lark-grammars',
    },
)
