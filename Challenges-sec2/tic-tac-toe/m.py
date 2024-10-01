from pwn import *

# Set up the context (optional)
#context(terminal=['tmux', 'new-window'])

# Start the process
p = process('./ttt')
c=0
d=0
# Function to generate or update the input variable
def update_input():
    # Update your variable logic here
    new_value=f"{c+1},{d+1}"
    return new_value  # Replace with your actual logic

# Main loop
while True:
    # Get the updated input
    input_value = update_input()

    # Send the input to the process
    p.sendline(input_value)

    # Optional: Receive and print the response
    response = p.recvline().decode().strip()
    print(response)

    # Sleep for a while before the next iteration
    sleep(1)  # Adjust the sleep time as needed
