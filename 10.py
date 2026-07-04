import numpy as np

try:

    n = int(input("Enter how many numbers you want to generate: "))

    a = np.random.randint(10, 101, n)

    # Print the array
    print("\n  Generated Array:")
    print(a)


    # Statistics
    print("\n Mean:", np.mean(a))
    print("Median:", np.median(a))
    print("Standard Deviation:", np.std(a))
    print("Minimum:", np.min(a))
    print("Maximum:", np.max(a))


    # Reshape into 2D array if possible
    if n % 2 == 0:
        b = a.reshape(2, n // 2)
        print("\n 2D Array:")
        print(b)

        print("\n Row-wise Sum:")
        print(np.sum(b, axis=1))
    else:
        print("\n Cannot reshape into a 2D array because the number of elements is odd.")

except ValueError:
    print("Please enter a valid number.")



    