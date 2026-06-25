
[![Runboat](https://img.shields.io/badge/runboat-Try%20me-875A7B.png)](https://runboat.odoo-community.org/builds?repo=OCA/server-brand&target_branch=18.0)
[![Pre-commit Status](https://github.com/OCA/server-brand/actions/workflows/pre-commit.yml/badge.svg?branch=18.0)](https://github.com/OCA/server-brand/actions/workflows/pre-commit.yml?query=branch%3A18.0)
[![Build Status](https://github.com/OCA/server-brand/actions/workflows/test.yml/badge.svg?branch=18.0)](https://github.com/OCA/server-brand/actions/workflows/test.yml?query=branch%3A18.0)
[![codecov](https://codecov.io/gh/OCA/server-brand/branch/18.0/graph/badge.svg)](https://codecov.io/gh/OCA/server-brand)
[![Translation Status](https://translation.odoo-community.org/widgets/server-brand-18-0/-/svg-badge.svg)](https://translation.odoo-community.org/engage/server-brand-18-0/?utm_source=widget)

<!-- /!\ do not modify above this line -->

# Nexus ERP - Debranded Retail & Marketplace Setup

This repository contains custom, debranded Odoo Community modules pre-configured for a 10-outlet retail Point of Sale system and a bilingual (Arabic/English) 10-vendor e-commerce portal with ZATCA compliance.

<!-- prettier-ignore-start -->

[//]: # (addons)

Available addons
----------------
addon | version | maintainers | summary
--- | --- | --- | ---
[debrand_retail_marketplace](debrand_retail_marketplace/) | 18.0.1.0.0 |  | Debranded Retail and Marketplace Setup
[disable_odoo_online](disable_odoo_online/) | 18.0.1.0.0 |  | Remove odoo.com Bindings
[portal_odoo_debranding](portal_odoo_debranding/) | 18.0.1.0.0 | <a href='https://github.com/eLBati'><img src='https://github.com/eLBati.png' width='32' height='32' style='border-radius:50%;' alt='eLBati'/></a> <a href='https://github.com/ivantodorovich'><img src='https://github.com/ivantodorovich.png' width='32' height='32' style='border-radius:50%;' alt='ivantodorovich'/></a> | Remove Odoo Branding from Website
[remove_odoo_enterprise](remove_odoo_enterprise/) | 18.0.1.0.0 |  | Remove enterprise modules and setting items

[//]: # (end addons)

<!-- prettier-ignore-end -->

---

## Installation & Deployment Guide

Follow these steps to deploy and run these modules on your server (**Host B**).

### 1. Manual Deployment

#### Step A: Clone the Repository on Host B
Navigate to your preferred applications directory and clone this repository:
```bash
cd /opt
sudo git clone https://github.com/khalilksa33/nexus.git
sudo chown -R odoo:odoo /opt/nexus
```

#### Step B: Add Custom Addons to Odoo Configuration
Open your Odoo configuration file (typically located at `/etc/odoo/odoo.conf`):
```bash
sudo nano /etc/odoo/odoo.conf
```
Append your cloned `/opt/nexus` directory to the `addons_path` variable:
```ini
addons_path = /var/lib/odoo/addons/18.0,/opt/nexus
```

#### Step C: Install the Modules
Restart the service to read the new path:
```bash
sudo systemctl restart odoo
```
Install the custom setup module from the terminal:
```bash
sudo -u odoo odoo -c /etc/odoo/odoo.conf -d YOUR_DATABASE_NAME -i debrand_retail_marketplace --stop-after-init
```

---

### 2. Configure the systemd Service (`nexus`)

To run Odoo under the branded system service name `nexus`:

1. Create a service file:
   ```bash
   sudo nano /etc/systemd/system/nexus.service
   ```
2. Paste the configuration:
   ```ini
   [Unit]
   Description=Nexus ERP Service
   After=postgresql.service

   [Service]
   Type=simple
   User=odoo
   Group=odoo
   ExecStart=/usr/bin/odoo -c /etc/odoo/odoo.conf
   KillMode=mixed
   Restart=always
   RestartSec=5

   [Install]
   WantedBy=multi-user.target
   ```
3. Load, enable, and start the service:
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl stop odoo
   sudo systemctl disable odoo
   sudo systemctl enable nexus
   sudo systemctl start nexus
   ```

---

### 3. Automated CI/CD Setup (GitHub Actions)

This repository includes a deployment workflow in `.github/workflows/deploy.yml` that routes SSH/SCP commands through a secure **Cloudflare Tunnel** using a **Service Token** to bypass authentication prompts automatically.

To configure the pipeline, add the following **secrets** to your GitHub repository (**Settings** -> **Secrets and variables** -> **Actions**):

| Secret Name | Description | Example Value |
| --- | --- | --- |
| `SSH_HOST` | Hostname routed by the Cloudflare Tunnel | `ssh-erp.26i.uk` |
| `SSH_USERNAME` | Login user name for Host B | `ubuntu` |
| `SSH_PRIVATE_KEY` | Private SSH key of the host user | `-----BEGIN OPENSSH PRIVATE KEY-----...` |
| `DEPLOY_PATH` | Path where nexus addons are deployed | `/opt/nexus` |
| `CF_CLIENT_ID` | Cloudflare Access Service Token Client ID | `abcd1234.access...` |
| `CF_CLIENT_SECRET` | Cloudflare Access Service Token Client Secret | `secret1234...` |

> **Note**: Ensure the Access application policy for `ssh-erp.26i.uk` in the **Cloudflare Zero Trust** console is configured with the Action type set to **`Service Auth`** for this Service Token.

---

## Licenses

This repository is licensed under [AGPL-3.0](LICENSE). Consult each module's `__manifest__.py` file for specific licenses.

