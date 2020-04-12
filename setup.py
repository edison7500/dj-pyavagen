from setuptools import setup

import dj_pyavagen

with open("README.md") as readme_file:
    readme = readme_file.read()

install_requires = (["Django>=1.11", "pyavagen>=0.3.3"],)

setup(
    name="django-pyavagen",
    version=dj_pyavagen.__version__,
    description="""Django Avatar gen""",
    long_description=readme,
    packages=["dj_pyavagen", "dj_pyavagen.templatetags", "dj_pyavagen.urls"],
    install_requires=install_requires,
    include_package_data=True,
    license="MIT License",
    zip_safe=False,
    keywords="django, avatar, python",
)
