# insta_catifier
A simple script that scrapes photos from your Instagram profile and replaces the faces on each of them with a cat face

### Prerequisites
- Python 3

### How to use
If you want just to use it then first run ```install.ps1``` in repository root folder. It will setup virtual environment and will install required libraries.

After that the script is ready to go:
```powershell
execute.ps1 <instagram profile name>
```

The script loads scraped Instagram photos to ```sources``` folder and catified photos to ```results``` folder.

### Example

![](https://raw.githubusercontent.com/DmitrievDmitriyA/insta_catifier/master/examples/88903499_1081213525575313_2384811281478813057_n.jpg "Before")
![](https://raw.githubusercontent.com/DmitrievDmitriyA/insta_catifier/master/examples/88903499_1081213525575313_2384811281478813057_n_catified.jpg "After")
