import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("VERSION", "r") as f:
    version = f.read().strip()

with open("requirements.txt") as f:
    install_requires = f.read().splitlines()

setuptools.setup(
    name="mifugo",
    version=version,
    author="Karim Kawambwa",
    author_email="karimkawambwa@gmail.org",
    description="Mifugo Ranch Manager APP.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/karimkawambwa/mifugo",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
    ],
)