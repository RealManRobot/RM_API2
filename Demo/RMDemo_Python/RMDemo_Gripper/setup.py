from setuptools import setup, find_packages

with open('readme.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='RMDemo_Gripper',  # Replace with your project name
    version='0.1.0',  # Replace with your project version
    description='Simulate object grasping, including grasping an object at a fixed position, moving to a designated '
                'position, controlling the gripper to apply continuous force for grasping, and after grasping the '
                'object, moving to the placement position and releasing it. Finally, return the robotic arm to the '
                'initial pose.',
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
