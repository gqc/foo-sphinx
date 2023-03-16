from setuptools import setup, find_packages

setup(
    name="foo",
    version='0.0.1',
    description="foo-package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Intended Audience :: Science/Research",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords="",
    url="https://github.com/deven367/test",
    author="Allen Institute for Artificial Intelligence",
    author_email="contact@allenai.org",
    license="Apache",
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"],
    ),
    package_data={"test_package": ["py.typed"]},
    install_requires=[],
    extras_require={"dev": []},
    python_requires=">=3.7",
)