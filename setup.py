from setuptools import setup, find_packages


def long_description():
    with open('README.rst', 'r') as f:
        return f.read()


setup(
    name='backcast',
    version='0.0.1',
    description='Backcast :: Textual summaries of past weather data',
    long_description=long_description(),
    author='Roman Kutlak',
    author_email='kutlak.roman@gmail.com',
    url='https://github.com/roman-kutlak/backcast',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha', 'Intended Audience :: Developers',
        'Intended Audience :: Science/Research', 'Natural Language :: English',
        'License :: OSI Approved :: MIT License', 'Operating System :: OS Independent',
        'Programming Language :: Python', 'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Text Processing :: Linguistic'
    ],
    packages=find_packages(exclude=['doc', 'tests/*', 'data']),
    keywords=['natural language generation', 'NLG', 'text generation', 'example'],
    install_requires=['nlglib'],
    extras_require={'dev': [
        'coverage',
        'nose',
        'rednose',
    ]},
    include_package_data=True,
    package_data={'backcast': ['data/*']},
    entry_points={
        'console_scripts': ['backcast=backcast.main:main'],
    },
    zip_safe=True,
)
