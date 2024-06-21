# DownloadAllFilesOnPage by @Julobulo

This tool allows you to download specific file types from a specified URL. Follow the steps below to use it effectively.

## Usage

### Step 1: Specify the URL

First, set the URL you want to scrape files from by typing:
```
url=https://thewebsitethatisgonnagetscraped.com
```

### Step 2: Specify the File Extensions

Next, indicate the file extensions you want to download. For example:
```
ext=.mp3,.mp4,.exe
```

### Step 3: Specify the Destination Folder

Finally, specify the destination folder where the downloaded files will be saved. If the folder does not exist, it will be created automatically. Use the following format:
```
destfolder=".\MyDestinationFolder"
```

### Example

A concrete example of running this script would be:
```
python downloadAllFilesOnPage.py url=https://theUrlYouWant.com ext=.mp3,.wav destfolder=".\MyDestinationFolder"
```

## Important Notes

- **Legal Use Only:** This script is designed to download only the specified file types from the provided URL. Ensure that you use this tool legally.
- **Anti-Scraping Measures:** This script is not designed to bypass advanced anti-scraping techniques. If you encounter a 429 error code (`print(request.status_code)`), it means the website has blocked the script. 

Enjoy using the tool responsibly!
