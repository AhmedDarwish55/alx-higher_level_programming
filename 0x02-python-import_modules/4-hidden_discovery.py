#!/usr/bin/python3
if __name__ == "__main__":
    """Print all hidden directories"""
    import hidden_4

    for i in range(hidden_4):
        if i[:2] != "__":
            print(i)
