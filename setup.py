from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(["src/main.py", "src/camera_buffer.py", "src/trigger_handler.py", "src/trigger_modbus.py"])
)