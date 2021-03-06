import io
from setuptools import setup
import flake8_quotes


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


long_description = read('README.rst')


setup(
    name='flake8-quotes',
    author='Zachary Wright Heller',
    author_email='zheller@gmail.com',
    version=flake8_quotes.__version__,
    install_requires=[
        'setuptools',
    ],
    url='http://github.com/zheller/flake8-quotes/',
    long_description=long_description,
    description='Flake8 lint for quotes.',
    py_modules=['flake8_quotes'],
    test_suite='test',
    include_package_data=True,
    entry_points={
        'flake8.extension': [
            'flake8_quotes = flake8_quotes:QuoteChecker',
        ],
    },
    license='MIT',
    zip_safe=True,
    keywords='flake8 lint quotes',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ]
)
