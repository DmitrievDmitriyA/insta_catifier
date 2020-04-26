import sys
import catifier.scraping as scraping
import catifier.enhancement as enhancement

def main():
    sourceFolder = 'sources\\'
    resultFolder = 'results\\'

    debugMode = False

    # Parse command arguments
    userName = sys.argv[1]
    try:
        if sys.argv[2] == '--debug':
            debugMode = True
    except:
        pass
    
    sourceUserFolder = sourceFolder + userName + '\\'
    resultUserFolder = resultFolder + userName + '\\'

    scraping.scrape_photos(sourceUserFolder)
    enhancement.add_cats(debugMode, userName, sourceUserFolder, resultUserFolder)

    print("Done!")

if __name__ == '__main__':
    main()