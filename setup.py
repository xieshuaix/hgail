from setuptools import setup, find_packages

setup(name='hgail',
      version='0.1',
      description='Generative Adversarial Imitation Learning',
      author='Blake Wulfe',
      author_email='wulfebw@stanford.edu',
      license='MIT',
      packages=[package for package in find_packages() if package.startswith('hgail')],
      zip_safe=False,
      install_requires=[
        'numpy==1.16.4',
        'rllab',
        'tensorflow==1.13.2',
        'gym',
        'h5py==2.10.0',
        'scipy==1.3.1',
        'cached_property==1.5.1',
        'joblib==0.13.2',
        ])
