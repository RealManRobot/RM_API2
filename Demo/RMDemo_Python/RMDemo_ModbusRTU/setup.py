from setuptools import setup, find_packages

with open('readme.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='RMDemo_ModbusRTU',  # Replace with your project name
    version='0.1.0',  # Replace with your project version
    description='Complete the configuration of the communication port in Modbus RTU mode, write single coil data, '
                'read single coil data, write a single register, read holding registers, and close the communication '
                'port in Modbus RTU mode.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'Robotic-Arm',  # Your project dependencies
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',  # Development status
        'Intended Audience :: Developers',  # Intended audience
        'License :: OSI Approved :: MIT License',  # License
        'Programming Language :: Python :: 3.9',  # Supported Python versions
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.9',  # Python version requirement
    keywords='robotic arm, automation, robotics',  # Add relevant keywords
)
