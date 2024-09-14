from setuptools import find_packages, setup

setup(
    name='chromatst',
    version='0.0.1',
    author='Yulia',
    author_email='ulechek.kul@gmail.com',
    install_requires=["openai","langchain", "langchain-community", "langchain-openai", 
                      "langchain-chroma",
                      "python-dotenv","pypdf", "chromadb","tiktoken"],
    packages=find_packages()

)