from setuptools import setup, find_packages

setup(
    name="smartrisk",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'matplotlib',
        'seaborn',
        'xgboost',
        'pytest',
        'dvc[gdrive]>=2.58.2,<3.0.0',
        'gdown>=4.7.1',
    ],
) 