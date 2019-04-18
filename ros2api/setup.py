from setuptools import find_packages
from setuptools import setup

package_name = 'ros2api'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name,package_name+".utils"],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='mwamp',
    author_email='mwamp@me.me',
    maintainer='mwamp',
    maintainer_email='mwamp@me.me',
    keywords=['ros2','rosapi','ros2_web_bridge','rosbridge_suite'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: TBD ',
        'Programming Language :: Python',
    ],
    description='Replicates rosapi from @rosbridge_suite for ros2',
    license='TBD',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'ros2api = ros2api.ros2api_node:main'
            
        ],
    },
)
