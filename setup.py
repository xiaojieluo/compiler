from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

packages = ['compiler']
test_requirements = ['pytest>=3.1.2']

setup(
    name='compiler',
    keywords='Automatically compile code based on file type',
    version='0.1.0',
    description='A data integrity check library',
    long_description=readme,
    author='Luo Xiaojie',
    author_email='xiaojieluoff@gmail.com',
    url='https://github.com/xiaojieluo/vlde',
    license=license,
    packages=packages,
    tests_require=test_requirements,
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ),
    test_suite='tests',
    python_requires='>=3',
)
