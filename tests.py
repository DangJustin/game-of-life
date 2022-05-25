from main import next_board_state


def test(input, output):
    next = next_board_state(input)
    if next == output:
        print("PASSED")
    else:
        print("FAILED")
        print("Expected:")
        print(input)
        print("Actual:")
        print(output)


if __name__ == "__main__":
    # TEST 1: dead cells with no live neighbors
    # should stay dead.
    init_state1 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    expected_next_state1 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    test(init_state1, expected_next_state1)

    # TEST 2: dead cells with exactly 3 neighbors
    # should come alive.
    init_state2 = [
        [0, 0, 1],
        [0, 1, 1],
        [0, 0, 0]
    ]
    expected_next_state2 = [
        [0, 1, 1],
        [0, 1, 1],
        [0, 0, 0]
    ]
    test(init_state2, expected_next_state2)
