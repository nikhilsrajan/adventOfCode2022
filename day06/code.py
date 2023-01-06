def get_marker_pos(filepath, N):
    with open('input.txt', 'r') as h:
        marker_pos = 0
        window = []
        while h:
            marker_pos += 1
            window.append(h.read(1))
            if len(window) == N:
                if len(set(window)) == N:
                    break
                window.pop(0)
    return marker_pos


start_of_packet = get_marker_pos('input.txt', N=4)
start_of_message = get_marker_pos('input.txt', N=14)

print('task 1:', start_of_packet)
print('task 2:', start_of_message)