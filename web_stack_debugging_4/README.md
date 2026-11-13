# Web stack debugging 4

Debugging project: find why Nginx failed many requests under load and automate the fix with Puppet.

## Files

| File | Description |
|---|---|
| `0-the_sky_is_the_limit_not.pp` | Puppet manifest that raises the Nginx open file limit from 15 to 4096 and restarts Nginx |

## Author

Ephrem Nziza
