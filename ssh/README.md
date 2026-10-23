# ssh

Scripts and configuration for connecting to a remote Ubuntu server over SSH
with an RSA key pair.

## Files

| File | What it does |
| --- | --- |
| `0-use_a_private_key` | Connects to the server as `ubuntu` with the key `~/.ssh/school` |
| `1-create_ssh_key_pair` | Creates a 4096-bit RSA key pair named `school`, protected by the passphrase `betty` |
| `2-ssh_config` | SSH client configuration that uses `~/.ssh/school` and refuses password authentication |
