### 1
```bash
docker compose -f /home/janus/greenbone-community-container/docker-compose.yml exec -it gsa bash
```
### 2
```bash
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    gnupg && \
    bash
```

### 3
```bash
apt-get update && apt-get install -y curl gnupg

NODE_KEYRING=/usr/share/keyrings/nodesource.gpg
NODE_VERSION=node_18.x
DISTRIBUTION=bookworm

curl -fsSL https://deb.nodesource.com/gpgkey/nodesource.gpg.key | gpg --dearmor | tee "$NODE_KEYRING" >/dev/null
echo "deb [signed-by=$NODE_KEYRING] https://deb.nodesource.com/$NODE_VERSION $DISTRIBUTION main" | tee /etc/apt/sources.list.d/nodesource.list

apt-get update && apt-get install -y nodejs
```

