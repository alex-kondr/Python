from setuptools import setup, find_namespace_packages

setup(
    name="clean",
    version="1",
    description="Sorts files for extention",
    url="https://github.com/alex-kondr/Python/tree/master/HW_07/clean_folder",
    autor="Alex Kondr",
    packages=find_namespace_packages(),
    entry_points={"console_scripts": ["clean-folder = clean_folder.clean:main"]},
)
