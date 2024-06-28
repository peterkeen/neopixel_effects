from setuptools import setup, find_packages

setup(
    name='neopixel_effects',
    version='0.1.0',
    description='a few interesting neopixel effects',
    url='http://github.com/peterkeen/neopixel_effects',
    author='peterkeen',
    author_email='',
    license='MIT',
    package_dir={"": "neopixel_effects"},
    packages=find_packages(where="neopixel_effects"),
    zip_safe=False,
    install_requires=[],
)
