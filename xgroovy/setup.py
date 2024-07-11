from setuptools import setup, find_packages

setup(
    name='xgroovy',
    version='0.1.0',
    description='A module for asynchronous web scraping and video downloading for xgroovy',
    author='codex-ML',
    packages=find_packages(),
    install_requires=[
        'pyppeteer',
        'asyncio'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

from setuptools import setup, find_packages

setup(
    name='xgroovy',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pyppeteer',
        'asyncio',
    ],
    entry_points={
        'console_scripts': [
            'scrape_videos=xgroovy.scraper:scrape_videos',
            'download_video=xgroovy.downloader:download_video',
        ],
    },
    author='codex-ML',
    description='An asynchronous web scraper and video downloader using pyppeteer',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/codex-ML/xgroovy',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
