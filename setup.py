from setuptools import setup

setup(
    name='sqlalchemy_pytest_fixtures',
    license='MIT',
    description='sqlachemy pytest fixtures',
    long_description='sqlachemy pytest fixtures',
    version='0.3.0',
    author='René Dudfield',
    author_email='renesd@gmail.com',
    url='http://github.com/illume/sqlalchemy_pytest_fixtures/',
    py_modules=['sqlalchemy_pytest_fixtures'],
    install_requires=['pytest>=2.0', 'sqlalchemy'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Software Development :: Testing',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        ]
)
