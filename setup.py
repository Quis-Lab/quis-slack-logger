"""
Setup script for slack-error-logger package.

This is an alternative to pyproject.toml for compatibility with older pip versions.
Modern pip will use pyproject.toml instead.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="slack-error-logger",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python library for centralized error logging to Slack via webhooks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/quis-slack-logger",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Logging",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.28.0",
        "python-dotenv>=0.19.0",
    ],
)

