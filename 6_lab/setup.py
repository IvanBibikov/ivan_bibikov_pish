from setuptools import setup, find_packages
setup(
    name="6_lab", 
    version="1.0.0",
    description="Собственный пакет, содержащий в себе функции для решения Лабораторной работы №2",
    author="Бибиков Иван Васильевич",
    author_email="bibikoviv.trtrans@gmail.com",
    packages=find_packages(),
    entry_points={ 
        "console_scripts": [
            "6_lab=6_lab.main:main",
        ],
    },
    
)