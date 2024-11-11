# A handheld device with communication system.
# To be able to communicate with the Elves, the device needs to lock on to their signal.
# Need to add a subroutine that detects the start-of-message marker.
# The start-of-message marker is a sequence of 14 characters that are all different.

seq = open("6-input.txt", 'r').read()

for i in range(len(seq)):
    if len(set(seq[i:i+14])) == 14:
        print(i+14)
        break