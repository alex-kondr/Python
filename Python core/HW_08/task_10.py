from collections import deque

MAX_LEN = 5

fifo = deque(maxlen=MAX_LEN)


def push(element):
    fifo.append(element)


def pop():
    return fifo.popleft()
