from setuptools import setup, find_packages

setup(
    name="forest_library_project",
    version="0.0.1",
    author="Felicia Tofan",
    author_email="tofan.felicia@gmail.com",
    url="",
    description="This is a simple Python library which download a Pytorch model.",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    entry_points={"console_scripts": ["forest_library_project = forest_library_project.main:download"]},
)
