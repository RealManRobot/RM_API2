from setuptools import setup, find_packages

with open('readme.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='RMDemo_MovejCANFD',  # Replace with your project name
    version='0.1.0',  # Replace with your project version
    description='Read the joint angle trajectory file under the demo, transmit it at a period of 10ms, and ensure '
                'stable operation of the robotic arm. For different models of robotic arms, register the callback '
                'function for real-time status, and during transmission, the current angle of the robotic arm can be '
                'obtained in real-time.',
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
