import setuptools

with open("README.md", "r",encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="downtool", 
    version="0.0.1",
    author="chen zhihan",
    license='MIT Licence',
    author_email="im.czh@qq.com",
    description="LogServer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/czhmisaka/LogServer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['requests','FastApi','uvicorn'],
    python_requires='>=3.6',
) 