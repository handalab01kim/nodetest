from setuptools import setup
from Cython.Build import cythonize

setup(
    # ext_modules=cythonize(["main.pyx","camera_buffer.py", "trigger_handler.py", "trigger_modbus.py"])
    ext_modules=cythonize(["main.py"])
)