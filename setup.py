from setuptools import setup
from pathlib import Path
from typing import List


SHORT_DESCRIPTION = 'Preprocessor template for `foliant init` command.'

try:
    with open('README.md', encoding='utf8') as readme:
        LONG_DESCRIPTION = readme.read()

except FileNotFoundError:
    LONG_DESCRIPTION = SHORT_DESCRIPTION

def get_templates(path: Path) -> List[str]:
    '''List all files in ``preprocessor`` directory, including all subdirectories.
    The resulting list contains UNIX-like relative paths starting with ``preprocessor``.
    '''

    result = []

    for item in path.glob('**/*'):
        if item.is_file() and not item.name.startswith('_'):
            result.append(item.relative_to(path.parent).as_posix())

    return result

setup(
    name='foliantcontrib.templates.preprocessor',
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    version='1.0.0',
    author='Konstantin Molchanov',
    author_email='moigagoo@live.com',
    url='https://github.com/foliant-docs/foliantcontrib.templates.preprocessor',
    packages=['foliant.cli.init.templates'],
    package_data={'foliant.cli.init.templates': get_templates(Path('foliant/cli/init/templates/preprocessor'))},
    license='MIT',
    platforms='any',
    install_requires=[
        'foliantcontrib.init>=1.0.5'
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Documentation",
        "Topic :: Utilities",
    ]
)
