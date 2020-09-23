import setuptools

with open("../README.md", "r") as fh:
    long_description = fh.read()

with open("../VERSION", "r") as vr:
    version_number = vr.read()

with open("../requirements.txt", "r") as req:
    requirements = []
    for l in req.readlines():
        requirements.append(l.rstrip())

setuptools.setup(
    name="python_wheel_boilerplate",
    version=version_number,
    author="Nex Sabre",
    author_email="nexsabre@protonmail.com",
    description="Automatically create and update a spack package base on the pypi.org information",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NexSabre/python-wheel-boilerplate",
    packages=setuptools.find_packages(),
    package_data={},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'python_wheel_boilerplate = python_wheel_boilerplate.main.main:main'
        ],
    },
)
