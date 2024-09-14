from setuptools import find_packages, setup

setup(
    name='vectordb',
    version='0.0.1',
    author='Yulia',
    author_email='ulechek.kul@gmail.com',
    install_requires=["openai","langchain", "langchain-community", "langchain-openai", "python-dotenv","pypdf", "pinecone-client","tiktoken"],
    packages=find_packages()

)