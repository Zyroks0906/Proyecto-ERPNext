from setuptools import setup, find_packages

setup(
    name="custom_app",
    version="0.0.1",
    description="App personalizada para carga de datos",
    author="Zyroks0906",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
