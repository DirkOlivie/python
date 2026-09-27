import json
import urllib.request


#source_id="FZJ-CMIP-ozone-1-2"
#source_id="FZJ-CMIP-ozone-h-1-0"
#source_id="FZJ-CMIP-ozone-hl-1-0"
source_id="FZJ-CMIP-ozone-m-1-0"
#source_id="FZJ-CMIP-ozone-vl-1-0"
#ource_id="IIASA-IAMC-vl-1-1-1"
#source_id="IIASA-IAMC-h-ext-1-1-1"     
#source_id="UOEXETER-ScenarioMIP-2-2-2"
#source_id="UofMD-landState-3-1-2"
#source_id="FZJ-CMIP-nitrogen-vl-1-0"
#source_id="FZJ-CMIP-nitrogen-m-1-0"
#source_id="FZJ-CMIP-nitrogen-hl-1-0"

direct_download_info_url = "https://raw.githubusercontent.com/PCMDI/input4MIPs_CVs/refs/heads/direct-download-links/direct-download-info/direct-download-info.json"
with urllib.request.urlopen(direct_download_info_url) as response:
    raw_response = response.read()
    direct_download_info = json.loads(raw_response)

data_of_interest = [
    v for v in direct_download_info if v["source_id"] == source_id
]
download_links = [v["download_link"] for v in data_of_interest]
print("You can then download the links with your tool of choice")
for dl in download_links:
    print(f"- {dl}")
