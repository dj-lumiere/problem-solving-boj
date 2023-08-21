# 2064 IP 주소

from functools import reduce
from sys import stdin


def input():
    return stdin.readline().strip()


def find_mask_digit(ip_address_min, ip_address_max, common_bits) -> int:
    result = 32
    for mid in range(32, -1, -1):
        range_min = ((2**32 - 1) ^ ((1 << mid) - 1)) & common_bits
        range_max = range_min + (1 << mid) - 1
        if range_min <= ip_address_min and ip_address_max <= range_max:
            result = mid
        else:
            break
    return result


def number_form(ip_address: str) -> int:
    ip_address_numbers = list(map(int, ip_address.split(".")))
    result = 0
    for v in ip_address_numbers:
        result += v
        result <<= 8
    result >>= 8
    return result


def ip_form(ip_address: int) -> str:
    ip_address_numbers = []
    for i in range(3, -1, -1):
        ip_address_sector = (ip_address & (255 << (8 * i))) >> (8 * i)
        ip_address_numbers.append(ip_address_sector)
    return ".".join(map(str, ip_address_numbers))


def find_mask(ip_addresses: list[int]) -> int:
    common_bits = reduce(lambda x, y: x & y, ip_addresses)
    mask_digit = find_mask_digit(min(ip_addresses), max(ip_addresses), common_bits)
    network_mask = (2**32 - 1) ^ ((1 << mask_digit) - 1)
    return network_mask


def find_network_address(ip_addresses, network_mask) -> int:
    common_bits = reduce(lambda x, y: x & y, ip_addresses)
    common_bits &= network_mask
    return common_bits


N = int(input())
ip_addresses: list[int] = [number_form(input()) for _ in range(N)]
network_mask = find_mask(ip_addresses)
network_address = find_network_address(ip_addresses, network_mask)
print(f"{ip_form(network_address)}\n{ip_form(network_mask)}")