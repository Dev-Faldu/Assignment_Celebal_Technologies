from src import lower_triangle, upper_triangle, pyramid

def main():
    print("Assigment-1: Triangle Pattern Generator")
    try:
        n = int(input("Enter the number of rows for the triangle: "))
        
        print("\n Lower Triangular Pattern")
        print(lower_triangle(n))
        
        print("\n Upper Triangular Pattern")
        print(upper_triangle(n))

        print("\n Pyramid Pattern")
        print(pyramid(n))

    except ValueError:
        print("Please enter a valid integer!")

if __name__ == "__main__":
    main()
