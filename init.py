import validate
import unzip

def main():

    validate_obj = validate.Validate()
    validate_obj.verify()

    unzip_obj = unzip.UnzipZip()
    unzip_obj.move_or_delete()

if __name__ == "__main__":
    main()
