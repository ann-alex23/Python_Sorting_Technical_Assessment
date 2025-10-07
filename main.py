def sort(width: float, height: float, length: float, mass: float) -> str:
    """
    Determines which stack a package should be dispatched to based on its
    volume, dimensions, and mass.

    """

    volume = width * height * length
    bulky = volume >= 1000000 or any(d >= 150 for d in (width, height, length))
    heavy = mass >= 20

    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"


# Example runs
if __name__ == "__main__":
    test_cases = [
        (100, 100, 100, 10),   
        (200, 50, 50, 10),     
        (50, 50, 50, 25),     
        (200, 200, 200, 25),   
    ]

    for i, (w, h, l, m) in enumerate(test_cases, 1):
        print(f"Test {i}: {sort(w, h, l, m)}")
