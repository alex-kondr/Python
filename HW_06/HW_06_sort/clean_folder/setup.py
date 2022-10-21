from setuptools import setup, find_namespace_packages

setup(
    name="clean",
    version="1",
    description="Sorts files for extention",
    url="https://github.com/alex-kondr/Python/tree/master/HW_06/HW_06_sort/sort_folder",
    autor="Alex Kondr",
    packages=find_namespace_packages(),
    entry_points={"console_scripts": ["clean-folder = clean_folder.clean:main"]},
    install_requires=["sys", "pathlib"]
)
