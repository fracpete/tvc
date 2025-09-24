from setuptools import setup, find_namespace_packages


def _read(f):
    """
    Reads in the content of the file.
    :param f: the file to read
    :type f: str
    :return: the content
    :rtype: str
    """
    return open(f, 'rb').read()


setup(
    name="tvc",
    description='"tandem version control" is a simple Python library for combining git and dvc commands that are typically issued in tandem.',
    long_description=(
            _read('DESCRIPTION.rst') + b'\n' +
            _read('CHANGES.rst')).decode('utf-8'),
    url="https://github.com/fracpete/tvc",
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Version Control',
        'Programming Language :: Python :: 3',
    ],
    license='MIT License',
    package_dir={
        '': 'src'
    },
    packages=find_namespace_packages(where='src'),
    install_requires=[
        "setuptools",
        "wai_logging>=0.0.5",
    ],
    version="0.0.1",
    author='Peter Reutemann',
    author_email='fracpete@gmail.com',
    entry_points={
        "console_scripts": [
            "tvc=tvc.app:sys_main",
        ],
    },
)

