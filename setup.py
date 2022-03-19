import setuptools

with open("requirements.txt", "r") as requirements:
    reqs = requirements.read().splitlines()

setuptools.setup(
    name='Fantasy Name Generator',
    version='0.1',
    description="A tool to automatically generate fantasy names.",
    keywords=["fantasy", "markov chain", "generation"],
    author="Benjamin M. Syiek",
    author_email="",
    packages=setuptools.find_packages(include=['fantasy_name_generator*']),
    include_package_data=True,
    install_requires=reqs,
    entry_points={
        'console_scripts': [
            'generate_name = fantasy_name_generator.scripts.generate_name:main'
        ],
    },
)
