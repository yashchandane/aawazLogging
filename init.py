import aawaz_parse
import validate
import unzip
import aawaz_logging


def main():

    validate_obj = validate.Validate()
    validate_obj.verify()

    unzip_obj = unzip.UnzipZip()
    unzip_obj.move_or_delete()

if __name__ == "__main__":
    main()
