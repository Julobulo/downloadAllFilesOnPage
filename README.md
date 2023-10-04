
-To use this tool by @Julobulo, you must first specify the url you want to get files from.
To do that, just type \"url=https://thewebsitethatisgonnagetscraped.com\"


-Then, you must specify the extensions you want to download.
To do that, just type "ext=.mp3,.mp4,.exe"


-Lastly, you need to indicate in which folder the downloaded are going to go.
To do that, just type \"destfolder=\".\\MyDestinationFolder\"\"

If the folder doesn't already exist, it is going to be created.

A concrete example of this script could be:
python downloadAllFilesOnPage.py url=https://theUrlYouWant.com ext=.mp3,.wav destfolder=".\\MyDestinationFolder"

NOTE: This python script DOES NOT download anything else than what is in the specified url! Use this script legally please!

PS: This script is not designedd to work against really developped ant-scrapping techniques, so if it doesn't work and that the error code is 429 (print(request.status_code)), it's just that the website has blocked the script...
Enjoy it!
