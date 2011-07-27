from setuptools import setup

setup(
  name="pump-flash",
  version="0.0.1",
  description="A Pump middleware for adding flash message support via sessions.",
  long_description=open("README.md").read(),
  author="Adeel Ahmad Khan",
  author_email="adeel@adeel.ru",
  py_modules=["pump_flash"],
  license="MIT")