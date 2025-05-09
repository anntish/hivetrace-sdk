from setuptools import setup, find_packages


def readme():
    with open("README.md", "r") as f:
        return f.read()


setup(
    name="hivetrace",
    version="1.2.1",
    author="Raft",
    author_email="sales@raftds.com",
    description="Hivetrace SDK for monitoring LLM applications",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="http://hivetrace.ai",
    packages=["hivetrace"],
    install_requires=["httpx>=0.28.1", "python-dotenv>=1.0.1"],
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
    ],
    keywords="SDK, monitoring, logging, LLM, AI, Hivetrace",
    python_requires=">=3.8",
)
