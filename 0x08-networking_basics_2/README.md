0x08. Networking basics #1

In computer networking, localhost is a hostname that refers to the current computer used to access it. The name localhost is reserved for loopback purposes. It is used to access the network services that are running on the host via the loopback network interface. Using the loopback interface bypasses any local network interface hardware.

0.0.0.0 is The Internet Protocol Version 4 address.

The hosts file is a plain text file that all operating systems use to translate hostnames (also known as web addresses or URLs) into IP addresses. When you type in a hostname, such as wikipedia.org, your system will look into the hosts file to get the IP address needed to connect to the appropriate server.

Project Requirements:
* **0. Change your home IP**
  * [0-change_your_home_IP](./0-change_your_home_IP): Bash script that configures an Ubuntu server as follows:
  * `localhost` resolves to `127.0.0.2`
  * `facebook.com` resolves to `8.8.8.8`

* **1. Show attached IPs**
  * [1-show_attached_IPs](./1-show_attached_IPs): Bash script that displays all active IPv4 IP's on the machine.

* **2. Port listening on localhost**
  * [100-port_listening_on_localhost](./100-port_listening_on_localhost): Bash script that listens on port `98` on `localhost`.
