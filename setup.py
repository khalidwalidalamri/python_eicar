from setuptools import setup, find_packages

setup(
    name="python_eicar",
    version="0.1",
    description="A python/pip package for testing antivirus detection for python packages and fasten testing using Eicar.",
    packages= find_packages(),
    install_requires=[],
    entry_points= {
        "console_scripts": [
            "eicar-print = python_eicar:eicar_print",
        ],
    },


)