import requests
from fake_useragent import UserAgent
from time import sleep
from random import randint
from bs4 import BeautifulSoup
import os

def getFileType(url: str, listOfTypes: list):
    try:
        import requests
        webPage = requests.head(url=url)
        # numberOfRequests += 1
        # print("Content-type found first try: {}".format(webPage.headers['Content-Type']))
        from mimetypes import guess_type
        contentType = webPage.headers['Content-Type']
        for type in listOfTypes:
            typeToTest = 'X' + type
            # print(typeToTest)
            if guess_type(typeToTest)[0] == None:
                # print('passing')
                continue
            # print("if {} in {}".format(guess_type(typeToTest)[0], contentType))
            if guess_type(typeToTest)[0] in contentType:
                return True
        return False
    except:
        return "broken link"

def downloadMP3(basisURL, lastURL, folderToDownload):
    # import os
    nameOfFile = lastURL.replace('%20', ' ')
    nameOfFile = nameOfFile.replace('%5b', '[')
    nameOfFile = nameOfFile.replace('%5d', ']')
    if os.path.exists(str(folderToDownload + "\\" +nameOfFile)):
        return "exists"
    urlToRequest = basisURL + lastURL
    try:
        r = requests.get(urlToRequest)
    except: # requests.exceptions.ChunkedEncodingError
        print("fuck {} not working".format(nameOfFile))
        return
    futureName = folderToDownload + "\\" + str(nameOfFile)
    
    from clint.textui import progress
    with open(futureName, 'wb') as f:
        total_length = int(r.headers.get('content-length'))
        for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
            if chunk:
                f.write(chunk)
                f.flush()
    return None


def downloadAllMP3onaPage(linkToPage, destinationPath, listOfExtensions):
    from time import time
    # set up a timer
    startTime = time()
    global numberOfRequests
    numberOfRequests = 0
    # Check whether the specified path exists or not and if not create a folder
    if not os.path.exists(destinationPath):
        print("creating this folder {}...".format(destinationPath))
        # Create a new directory because it does not exist
        os.makedirs(destinationPath)
        print("Directory created!\n")
    
    numberOfDownloadedFiles = 0
    # link = "http://www.ashleecadell.com/xyzstorelibrary/" + linkToPage
    # generate a random useragent
    headers = {"User_Agent":UserAgent().random}
    # request the url to have the webPage stored in the programm
    try:
        webPage = requests.get(linkToPage, headers=headers)
        numberOfRequests += 1
    except requests.exceptions.ChunkedEncodingError:
        print("fuck this link {} is not working".format(linkToPage))
    timeOfDelay = 10
    # waiting for the status_code to 
    while webPage.status_code == 429 or webPage.status_code != 200:
        webPage = requests.get(linkToPage) #, headers=headers
        numberOfRequests += 1
        print("sleeping {} because of f**ing server blocking services status_code: {}".format(timeOfDelay, webPage.status_code))
        sleep(timeOfDelay)
        timeOfDelay += randint(timeOfDelay, timeOfDelay*timeOfDelay)
    

    soup = BeautifulSoup(webPage.text, 'html.parser')
    for link in soup.findAll('a'):
        try:
            # download the file if it has any of the extensions in list
            if getFileType(str(linkToPage + link['href']), listOfExtensions):
            # for extension in listOfExtensions:
            #     if link['href'].endswith(extension):
                print("Donwloading this file: {}...".format(link['href']))
                # if the file already exists...
                if not downloadMP3(linkToPage, link['href'], destinationPath) == "exists":
                    print("This file downloaded!: {}\n".format(link['href']))
                    numberOfDownloadedFiles += 1
                else:
                    print("This file already exists!: {}\n".format(link['href']))
        except KeyError:
            pass
    totalTime = round(time()-startTime)
    return (numberOfDownloadedFiles, numberOfRequests, totalTime)

"""
-pouvoir preciser l'url avec url=urltodownload
-pouvoir preciser les extensions avec ext=.extension,.otherextension
-pouvoir preciser le dossier de destination avec destfold=destinationfolder
"""

import sys

# get the name of the script
pythonFileName = os.path.basename(__file__)

# Describe how to use the script
if "--help" in sys.argv:
    print("\n-To use this tool by Julobulo, you must first specify the url you want to get files from.")
    print("To do that, just type \"url=https://thewebsitethatisgonnagetscraped.com\"\n")
    print("\n-Then, you must specify the extensions you want to download.")
    print("To do that, just type \"ext=.mp3,.mp4,.exe\"\n")
    print("\n-Lastly, you need to indicate in which folder the downloaded are going to go.")
    print("To do that, just type \"destfolder=\".\\MyDestinationFolder\"\"\n")
    print("If the folder doesn't already exist, it is going to be created.")
    print("\nA concrete example of this script could be:")
    print("python {}.py url=https://theUrlYouWant.com ext=.mp3,.wav destfolder=\".\\MyDestinationFolder\"\n".format(pythonFileName))
    print("\nNOTE: This python script DOES NOT download anything else than what is in the specified url! Use this script legally please!\n")
    exit()

# If no arguments are specified
if sys.argv == None:
    print("To get help, just type \"python {}.py --help\"".format(pythonFileName))
    exit()

# organize the specified arguments
for argument in sys.argv:
    # if the argument name is the name of the python file then skip it
    if argument == pythonFileName or pythonFileName in argument:
        continue
    # split the argument give at the "="
    argumentList = argument.split("=")
    # if there is nothing after the "=" sign or that no "=" sign was written then just give an error message
    if len(argumentList) != 2:
        print("\n{}: Arguments not valid!\n".format(argument))
        exit()
    if argumentList[0].lower() == "url":
        if not argumentList[1].startswith("http"):
            print("Not valid url! (hint: type the entire url, with https://...)")
            exit()
        urlToDownload = argumentList[1]
    elif argumentList[0].lower() == "ext":
        if not argumentList[1].startswith('.'):
            print("Not valid file extensions! (hint: file extension could be: .mp3,.mp4,.exe)")
            exit()
        listOfext = argumentList[1].split(',')
    elif argumentList[0].lower() == "destfolder":
        destinationFolder = argumentList[1]
    # if the arguments is none of the above, give an error with the argument's name and stop the program
    else:
        print("\n{}: Invalid argument!\n".format(argument))
        exit()


print("\nGoing to download this url {}...".format(urlToDownload))
print("This programs will download all the files with the following file extensions: {}.".format(listOfext))
print("The destination folder for the downloaded files is: {}.\n".format(destinationFolder))
print("\nStarting download...")

tupleOfProgram = downloadAllMP3onaPage(urlToDownload, destinationFolder, listOfext)
print("The program downloaded {} files\nThis Program made {} requests, in {} seconds.",
      "\nDon't forget that the count did not include the requests made to the files."
      .format(tupleOfProgram[0], tupleOfProgram[1], tupleOfProgram[2]))
