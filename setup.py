import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="report",
    version="0.0.1",
    author="Oleg Izvolov",
    author_email="author@example.com",
    description="That application that takes a string and returns the number of unique characters in the string",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.foxminded.com.ua/Oleg-Izvolov/task-6-report-of-monaco-2018-racing",
    project_urls={
        "Bug Tracker": "https://git.foxminded.com.ua/Oleg-Izvolov/task-6-report-of-monaco-2018-racing/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "report"},
    packages=setuptools.find_packages(where="report"),
    python_requires=">=3.6",
)