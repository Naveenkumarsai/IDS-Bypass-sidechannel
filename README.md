# IDS-Bypass-sidechannel
A project demonstrating IDS/IPS bypass using timing and side-channel evasion techniques
This project demonstrates how attackers can bypass signature-based IDS systems like Suricata using timing delays, packet fragmentation, and encoding strategies.

# Technologies Used
- Flask (Vulnerable Web App)
- Suricata IDS
- Python (Automation Scripts)
- Wireshark (Traffic Analysis)
- Curl & Requests

 # Folder Structure
- `app.py`: Flask web app with timing vulnerability
- `bypass.py`: Script to extract secret using time-based side-channel attack
- `rules/local.rules`: Suricata rule to detect SQL injection
- `docs/`: Project documentation
- `screenshots/`: Testing outputs and diagrams

 # How to Run

```bash
sudo apt update && sudo apt install python3-pip suricata
pip3 install flask requests

python3 app.py
sudo suricata -c /etc/suricata/suricata.yaml -i eth0 --af-packet

# In another terminal
python3 bypass.py
