# install paddlepaddle
# ref: https://www.paddlepaddle.org.cn/install/quick?docurl=/documentation/docs/zh/install/pip/linux-pip.html
python3 -m pip install paddlepaddle-gpu==2.6.0.post120 -f https://www.paddlepaddle.org.cn/whl/linux/mkl/avx/stable.html

# Issue#1:
Error: Can not import paddle core while this file exists: /home/user/anaconda3/envs/nn/lib/python3.11/site-packages/paddle/base/libpaddle.so ... ImportError: /home/user/anaconda3/envs/nn/bin/../lib/libstdc++.so.6: version `GLIBCXX_3.4.30' not found (required by /home/user/anaconda3/envs/nn/lib/python3.11/site-packages/paddle/base/libpaddle.so)

Solution:
conda install conda-forge::gcc

# Issue#2:
W0223 21:51:32.722573 40247 gpu_resources.cc:119] Please NOTE: device: 0, GPU Compute Capability: 8.6, Driver API Version: 12.2, Runtime API Version: 12.0
W0223 21:51:32.722811 40247 dynamic_loader.cc:314] The third-party dynamic library (libcudnn.so) that Paddle depends on is not configured correctly. (error code is /usr/local/cuda/lib64/libcudnn.so: cannot open shared object file: No such file or directory)
  Suggestions:
  1. Check if the third-party dynamic library (e.g. CUDA, CUDNN) is installed correctly and its version is matched with paddlepaddle you installed.
  2. Configure third-party dynamic library environment variables as follows:
  - Linux: set LD_LIBRARY_PATH by `export LD_LIBRARY_PATH=...`
  - Windows: set PATH by `set PATH=XXX;
Traceback (most recent call last):
  File "/home/user/Desktop/workspace_diffusion/4_pp_matting_torch/z_unit_tests_pp2torch/a_pp_vs_torch_tensor.py", line 19, in <module>
    im_p = paddle.transpose(im_p, perm=[2,0,1])
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/user/anaconda3/envs/nn/lib/python3.11/site-packages/paddle/tensor/linalg.py", line 87, in transpose
    return _C_ops.transpose(x, perm)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: (PreconditionNotMet) Cannot load cudnn shared library. Cannot invoke method cudnnGetVersion.
  [Hint: cudnn_dso_handle should not be null.] (at ../paddle/phi/backends/dynload/cudnn.cc:60)

Solution:
# Downgrade the version
python3 -m pip install paddlepaddle-gpu==2.6.0.post112 -f https://www.paddlepaddle.org.cn/whl/linux/cudnnin/stable.html
