import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name = "test-python-library",
    version ='0.0.2',
    author = "Anuj Panthri",
    author_email="panthrianuj@gmail.com",
    description="just a sample library",
    long_description=long_description,
    long_description_content_type = "text/markdown",
    
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)