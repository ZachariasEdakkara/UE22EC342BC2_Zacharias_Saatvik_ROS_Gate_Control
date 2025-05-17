from setuptools import setup

package_name = 'gate_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],  # <-- THIS IS THE FIX
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools','visualization_msgs'],
    zip_safe=True,
    maintainer='zacharias',
    maintainer_email='zacharias@todo.todo',
    description='Opens a gate using an ultrasonic sensor and servo motor with Arduino + ROS 2',
    license='MIT',  # Optional: choose an open-source license if you'd like
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'gate_control_node = gate_control.gate_control_node:main',
        ],
    },
)
