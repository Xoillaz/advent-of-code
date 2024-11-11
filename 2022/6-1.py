# A handheld device with communication system.
# To be able to communicate with the Elves, the device needs to lock on to their signal.
# Need to add a subroutine that detects the start-of-packet marker.
# The start-of-packet marker is a sequence of four characters that are all different.

seq = open("6-input.txt", 'r').read()

for i in range(len(seq)):
    if len(set(seq[i:i+4])) == 4:
        print(i+4)
        break