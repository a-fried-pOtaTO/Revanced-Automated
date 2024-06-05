import pexpect

# Spawn a child process to run a simple command
child = pexpect.spawn('echo Hello, World!')

# Wait for the command to complete
child.expect(pexpect.EOF)

# Print the output
print(child.before.decode('utf-8'))
