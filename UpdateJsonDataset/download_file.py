import urllib.request


def download_file(source, destination):
    try:
        urllib.request.urlretrieve(source, destination)
    except IOError:
        print('IOError: An error occured trying to write an updated spreadsheet.')
        print('Do you already have it open?')
    except urllib.error.URLError:
        print('URLError: An error occured trying to download the file. \
                Please check the source and try again.')
