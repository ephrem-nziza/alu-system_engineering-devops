# Firewall

Firewall project for the web stack of `ephremnziza.tech`.

## Files

| File | Description |
|---|---|
| `0-block_all_incoming_traffic_but` | Installs `ufw` on web-01 and blocks all incoming traffic except TCP ports 22 (SSH), 80 (HTTP) and 443 (HTTPS) |

## Rules applied on web-01

```bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
```

Port 22 is allowed before the firewall is enabled so the SSH session is not cut off.

## Servers

| Name | IP |
|---|---|
| 7380-web-01 | 35.177.53.215 |
| 7380-web-02 | 13.40.95.4 |
| 7380-lb-01 | 18.175.244.5 |

## Author

Ephrem Nziza
