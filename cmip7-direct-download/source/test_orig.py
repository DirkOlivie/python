import json
import urllib.request

direct_download_info_url = "https://raw.githubusercontent.com/PCMDI/input4MIPs_CVs/refs/heads/direct-download-links/direct-download-info/direct-download-info.json"
with urllib.request.urlopen(direct_download_info_url) as response:
    raw_response = response.read()
    direct_download_info = json.loads(raw_response)

data_of_interest = [
    v for v in direct_download_info if v["source_id"] == "FZJ-CMIP-ozone-vl-1-0"
]
download_links = [v["download_link"] for v in data_of_interest]
print("You can then download the links with your tool of choice")
for dl in download_links:
    print(f"- {dl}")
