# Web stack debugging 3

Debugging project: use `strace` to find why Apache returned a 500 error on a WordPress site, and automate the fix with Puppet.

## Files

| File | Description |
|---|---|
| `0-strace_is_your_friend.pp` | Puppet manifest that fixes the `.phpp` typo in `wp-settings.php` |

## Author

Ephrem Nziza
