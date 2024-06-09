from setuptools import setup, find_packages

setup(
    name="gpt_query",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "openai",
        "python-dotenv"
    ],
    author="Julien Mousqueton",
    author_email="julien+github@mousqueton.io",
    description="A library to query OpenAI's GPT-4 model",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/jmousqueton/gpt_query",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
