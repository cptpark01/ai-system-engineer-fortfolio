## apt update / net-tools install failure on Ubuntu VM

**Problem**
- `apt update` failed with "Some index files failed to download"
- Package installation was blocked

**Root Cause**
- DNS resolution instability in VirtualBox NAT environment

**Resolution**
- Configured static DNS via netplan
- Cleaned APT cache and refreshed package index

```bash
sudo rm -rf /var/lib/apt/lists/*
sudo netplan apply
sudo apt update

Outcome
* Successfully installed net-tools
