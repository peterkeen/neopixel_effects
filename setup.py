from setuptools import setup, find_packages

setup(
    name='neopixel_effects',
    version='0.1.0',
    description='a few interesting neopixel effects',
    url='http://github.com/peterkeen/neopixel_effects',
    author='peterkeen',
    author_email='',
    license='MIT',
    package_dir={"": "."},
    packages=find_packages(where="."),
    zip_safe=False,
    install_requires=[],
)
