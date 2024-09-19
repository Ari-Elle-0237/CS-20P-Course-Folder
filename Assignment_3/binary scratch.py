# bits_a = 0b10110101
# bits_b = 0b10111101
bits_a = 0b10110101
bits_b = 0b10110111

xor_ab = bits_b ^ bits_a
print(f"{xor_ab:08b}")
# print(bin(bits_b ^ bits_a))
# print(xor_ab.bit_count())
print(bin(xor_ab).count("1"))
print(xor_ab.bit_length())
print(xor_ab.bit_count())


def compare_bits(bits_a, bits_b):
    # XOR A and B together, then count the number of ones in the resulting binary number to determine
    # the number of differences between
    # If your script is running earlier than python 3.10 then it should be bin(bits_a).count("1")
    bit_count = (bits_a ^ bits_b).bit_count()
    print(f"{bit_count=}")
    if bit_count <= 7:
        return bit_count
    return -1

print(list(enumerate(range(4,11))))

# https://www.geeksforgeeks.org/count-set-bits-using-python-list-comprehension/


print(compare_bits(bits_a,bits_b))


if __name__ == "__main__":
    pass