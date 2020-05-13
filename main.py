import sys
import catifier.scraping as scraping
import catifier.enhancement as enhancement


def main():
    sourceFolder = 'sources/'
    resultFolder = 'results/'

    # Parse command arguments
    userName = sys.argv[1]

    sourceUserFolder = sourceFolder + userName + '/'
    resultUserFolder = resultFolder + userName + '/'

    scraping.scrape_photos(sourceUserFolder)
    enhancement.add_cats(sourceUserFolder, resultUserFolder)

    print("Done!")


if __name__ == '__main__':
    main()
