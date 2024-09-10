from setuptools import setup, find_packages

with open("app/README.md", "r") as f:
    long_description = f.read()

setup(
    name="MERNcraft",
    version="1.0.2",
    author="Hardik Pawar",
    author_email="hardikpawarh@gmail.com",
    description="MERNcraft is an automation script designed to kickstart your MERN stack application development. It helps you set up a basic project structure with React for the frontend and Express for the backend.",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hardvan/MERNcraft",
    keywords=["automation", "mern", "project",
              "create-react-app", "express", "mongodb"],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
