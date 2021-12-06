import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A9Q2DjI9eMlvuuMPTn7fNC6olXDLPewxAcKFklWEhSUFnle8K_7SNUFZoWKHn5nL1HgnZJmzQ1ZswA0OqVAvNF1_yfavftfLQk969Gfm-A1gFRcfq5dJVu8B0mgDTQbzQL386I0dYlA'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("Enter the full path to upload to dropbox:- ")

    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")
main()