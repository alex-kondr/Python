from setuptools import setup, find_namespace_packages

setup(
    name = "my first bot",
    version = "1.0.0",
    author = "Alex Kondr",
    url = "https://github.com/alex-kondr/Python/tree/master/HW_09/console_bot",
    license = "MIT License",
    packages = find_namespace_packages(),
    entry_points = {"console_scripts": ["my_bot = console_bot.bot:main"]}
)