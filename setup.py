
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='SunFounder_Emo',

    version='1.0.0',

    description='The class for SunFounder Emo',
    long_description=long_description,

    url='https://github.com/sunfounder/SunFounder_Emo',

    author='SunFounder',
    author_email='service@sunfounder.com',

    license='GNU',

    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='raspberry pi LED matrix SunFounder Emo',

    packages=find_packages(exclude=['docs', 'examples']),

    install_requires=['spidev'],

    entry_points={
        'console_scripts': [
            'sunfounder_emo=SunFounder_Emo:main',
        ],
    },
)
