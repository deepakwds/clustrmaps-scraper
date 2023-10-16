[**Clustrmaps Scraper**](https://github.com/deepakwds/clustrmaps-scraper)

Step1: 
**Input** - Sno, ID, Link
Run a script 
python clustermap_localities_scraping.py
**Output** - Sno, ID, Output Link (Create Localities Link Eg- https://clustrmaps.com/d/CA/Oakland)

Step2: 
**Input** - Sno, ID, Output Link (Can be collected from Localities_Out.txt from the above output)
Run a script 
python clustermap_FIPS_scraping.py
**Output** - Sno, ID, Output Link

Step3: 
**Input** - Sno, ID, Output Link (Can be collected from FIPS_Out.txt from the above output)
Run a script 
python clustermap_FIPS_scraping.py
**Output** - Id, Sku, Link, Name, Locality_Age, Address, P_Phone, Email

**Contribution**
[Buy me a coffee](https://www.buymeacoffee.com/deepakwds7)https://www.buymeacoffee.com/deepakwds7
