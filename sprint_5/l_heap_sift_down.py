def sift_down(heap, idx) -> int:
    left_idx = idx * 2
    right_idx = idx * 2 + 1

    if left_idx >= len(heap):
        return idx
    if right_idx < len(heap) and heap[right_idx] > heap[left_idx]:
        largest_idx = right_idx
    else:
        largest_idx = left_idx

    if heap[idx] < heap[largest_idx]:
        heap[idx], heap[largest_idx] = heap[largest_idx], heap[idx]
        return sift_down(heap, largest_idx)
    return idx


def test():
    sample = [-1, 12, 1, 8, 3, 4, 7]
    assert sift_down(sample, 2) == 5


if __name__ == "__main__":
    test()
