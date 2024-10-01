# Convert string to bytes using UTF-8 encoding
string_data = "0,0"
bytes_data = string_data.encode('utf-8')

# Example usage with pwntools
from pwn import *
dt=b"0,0"
# Start a process running the 'example_binary'
p = process('./ttt')

# Send bytes data
#p.sendline(dt)

# Receive output
output = p.recvall()

# Print the output
print(output.decode('utf-8'))

# Close the process
p.close()
