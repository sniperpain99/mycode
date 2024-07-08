def bottles_of_beer():
    for i in range(99, 0, -1):
        print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
        print(f"Take one down and pass it around, {i-1 if i > 1 else 'no more'} bottles of beer on the wall.\n")
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Go to the store and buy some more, 99 bottles of beer on the wall.\n")

if __name__ == "__main__":
    bottles_of_beer()

