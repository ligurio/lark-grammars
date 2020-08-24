import setuptools

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="lark-grammars",
    version="0.3.0",
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
