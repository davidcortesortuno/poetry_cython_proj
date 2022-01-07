import setuptools
from setuptools.extension import Extension
from Cython.Distutils import build_ext
# import sys
# cython and python dependency is handled by pyproject.toml
from Cython.Build import cythonize
import numpy


# -----------------------------------------------------------------------------


# Compilation of C module in c_lib
com_args = ['-std=c99', '-O3', '-fopenmp']
link_args = ['-fopenmp']
extensions = [
    Extension("pcython_proj.cython_lib.example_cython",
              ["pcython_proj/cython_lib/example_cython.pyx",
               "pcython_proj/cython_lib/example.c"],
              # extra_compile_args={'gcc': com_args},
              extra_compile_args=com_args,
              extra_link_args=link_args,
              include_dirs=[numpy.get_include()]
              )
]


# -----------------------------------------------------------------------------


class BuildExt(build_ext):
    def build_extensions(self):
        try:
            super().build_extensions()
        except Exception:
            pass


def build(setup_kwargs):
    setup_kwargs.update(
        dict(
            cmdclass=dict(build_ext=BuildExt),
            ext_modules=cythonize(extensions,
                                  language_level=3),
            zip_safe=False
        )
    )
