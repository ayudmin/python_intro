def make_sandwich(*items):
    print(f"\nMaking sandwich with the following items:")
    for item in items:
        print(f"- {item}")

make_sandwich('potatoes', 'bread')
make_sandwich('groundnut paste', 'chappati')