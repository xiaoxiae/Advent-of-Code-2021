import sys

sys.path.insert(0, "../")
from utilities import success, get_input

from typing import *


def hex_to_bin(c: int) -> str:
    """Return a 4-bit binary number from a hex digit."""
    return bin(int(c, 16))[2:].rjust(4, "0")


def trim_to_byte(packet) -> str:
    """Trim the leftover bits from the start so the packet contains whole bytes."""
    return packet[len(packet) % 4 :]


def get_int_from_packet(packet, n) -> (int, str):
    """Return the n-bit number from n MSb of the packet and the rest of the packet."""
    return int(packet[:n], 2), packet[n:]


def parse_literal(packet) -> (int, str):
    """Parse a literal from the packet, returning it and the remaining packet."""
    num_bin = ""
    while packet[0] != "0":
        num_bin += packet[1:5]
        packet = packet[5:]
    num_bin += packet[1:5]

    return int(num_bin, 2), packet[5:]


version_sum = 0


def parse_packet(packet) -> [List, str]:
    global version_sum

    version, packet = get_int_from_packet(packet, 3)
    type_id, packet = get_int_from_packet(packet, 3)

    version_sum += version

    # literal
    if type_id == 4:
        literal, packet = parse_literal(packet)

        return literal, packet

    # operator
    else:
        length_type_id, packet = get_int_from_packet(packet, 1)

        results = []

        if length_type_id == 0:
            subpacket_bits, packet = get_int_from_packet(packet, 15)

            original_packet_length = len(packet)

            while original_packet_length - len(packet) != subpacket_bits:
                result, packet = parse_packet(packet)
                results.append(result)
        else:
            subpacket_count, packet = get_int_from_packet(packet, 11)

            results = []

            for _ in range(subpacket_count):
                result, packet = parse_packet(packet)
                results.append(result)

        return results, packet


packet = get_input()[0]
packet_bin = "".join([hex_to_bin(c) for c in packet])

parse_packet(packet_bin)

success(version_sum)
