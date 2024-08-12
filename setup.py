from setuptools import setup, find_packages

setup(
    name='Valerian and the quest for Thaemus',
    version='0.1.0',
    description='A text-based adventure game',
    author='TechVoyager01',
    author_email='d.b.lousteau@gmail.com',
    packages=find_packages(where='save_game_file'),
    package_dir={'': 'save_game_file'},
    install_requires=[
        'os',
        'collections',
        'random',
        'pytest',  # Add any other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'valerian_and_the_quest_for_thaemus=main:main',  # Adjust if the main entry point is different
        ],
    },
)