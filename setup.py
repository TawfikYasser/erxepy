import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="erxepy",
    version="0.0.1",
    author="Tawfik Yasser",
    author_email="tawfekyassertawfek@gmail.com",
    description="Easy Regular Expression Python Module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TawfikYasser/erxepy",
    project_urls={
        "Bug Tracker": "https://github.com/TawfikYasser/erxepy/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)