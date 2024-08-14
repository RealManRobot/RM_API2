from setuptools import setup, find_packages

with open('readme.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='RMDemo_Lift',  # Replace with your project name
    version='0.1.0',  # Replace with your project version
    description='Control the lift to move to a specified height in a non-blocking manner, while simultaneously '
                'controlling the robotic arm to move to the pre-grasping position. The robotic arm performs a forward '
                'move with movel for a certain distance, then controls the gripper to apply continuous force for '
                'grasping. After grasping the object, the robotic arm performs a backward move with movel for a '
                'certain distance to return to the pre-grasping position. Then, control the lift to move to another '
                'height in a blocking manner. Once the lift reaches the position, the robotic arm performs a forward '
                'move with movel for a certain distance, controls the gripper to release the grasp, and after '
                'releasing the object, the robotic arm performs a backward move with movel for a certain distance to '
                'return to the pre-grasping position.',
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
