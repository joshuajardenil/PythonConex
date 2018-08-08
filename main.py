from PythonConex import PythonConex

# Main Function
if __name__ == "__main__":
    instrumentKey = "COM25"
    pythonConex = PythonConex(instrumentKey)
    pythonConex.move_absolute(3.0)