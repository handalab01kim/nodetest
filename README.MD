## dependencies
pip install opencv-python pymodbus==2.5.3
<!-- pip install opencv-python==4.12.0.88 pymodbus==2.5.3 -->

## 난독화
pip install setuptools cython
<!-- python setup.py build_ext --inplace -->
python setup.py build_ext --build-lib release/libs