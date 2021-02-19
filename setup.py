import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gocomet-task",
    version="0.0.1",
    author="Sreyans Singhi",
    author_email="shreyanssinghi11@gmail.com",
    description="GoComet assignment package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: NA :: NA",
        "Operating System :: OS Independent"
        ],
    python_requires='>=3.6',
)
