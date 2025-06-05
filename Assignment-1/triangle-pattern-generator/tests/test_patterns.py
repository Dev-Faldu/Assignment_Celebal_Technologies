from src import lower_triangle, upper_triangle, pyramid

def test_lower_triangle():
    assert lower_triangle(2) == "* \n* *"

def test_upper_triangle():
    assert upper_triangle(2) == "* *\n  *"

def test_pyramid():
    assert pyramid(2) == " * \n* *"

if __name__ == "__main__":
    test_lower_triangle()   
    test_upper_triangle()
    test_pyramid()
    print("All pattern tests passed.")
