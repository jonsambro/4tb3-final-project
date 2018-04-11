# Dependencies:
1. Python 3
2. Python packages listed in requirements.txt. Run pip install -r requirements.txt from this directory to install them.
3. antlr4 is required to generate the grammar defined in src/Parallelize/Parallelize.g4 but not required to run the application with a pre-generated grammar (sudo apt-get install antlr4 on ubuntu)

# Example programs
python3 src/loop_parallelize.py test/integrate.cpp
python3 src/loop_parallelize.py test/fib.cpp