from setuptools import setup

version = '1.3.dev0'

install_requires = [
    'cookiecutter',
    ]

tests_require = [
    'coverage',
    'nose',
    ]

setup(
    name='cookiecutter-djangosite-template',
    packages=[],
    version=version,
    description='Cookiecutter template for a Python package',
    author='Reinout van Rees',
    license='MIT',
    author_email='reinout@vanrees.org',
    url='https://github.com/nens/cookiecutter-djangosite-template',
    keywords=['cookiecutter', 'template', 'package', ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development',
    ],
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require = {'test': tests_require},
)
