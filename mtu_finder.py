import subprocess
import ipaddress
import argparse
import socket

HEADERS_SIZE = 28


def ping_host(host, packet_size):
    process = subprocess.run(
        ["ping", host, "-M", "do", "-s", packet_size, "-c", "1"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
        # capture_output=True,
        # text=True
    )
    return process.returncode


def find_mtu(host):
    left = 1
    right = 10**4
    while right - left >= 2:
        mtu = (left + right) // 2
        print("Current left = ", left, " | Right = ", right, " | mtu = ", mtu)
        if ping_host(host, str(mtu)) == 0:
            left = mtu
        else:
            right = mtu
    print("Result: ", left)
    return left


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('host')
    args = parser.parse_args()
    hostname = args.host
    host = socket.gethostbyname(hostname)

    try:
        ipaddress.ip_address(host)
    except:
        print("Host is not valid exception for host = ", host)
        exit(1)

    try:
        assert ping_host(hostname, "1") == 0
    except:
        print("Bad response (returncode) for host = ", host)
        exit(1)

    mtu = find_mtu(host)
    print("MTU =", mtu + HEADERS_SIZE)


if __name__ == '__main__':
    main()


