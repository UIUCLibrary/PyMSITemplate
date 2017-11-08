import os
# import shutil
# import uuid
#
#
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def create_license(licenses_text):
    print("Generating LICENSE.rtf file")
    paragraphs = licenses_text.split("\n\n")

    with open("windows_build/LICENSE.rtf", "w") as w:
        w.write("{\\rtf1\\ansi\\deff0{\\fonttbl{\\f0 \\fswiss Helvetica;}{\\f1 Courier;}}\n")
        w.write("\\widowctrl\\hyphauto")
        for paragraph in paragraphs:

            w.write("{\\pard \\q1 \\sa180 \\li0 \\fi0")
            w.write(paragraph)
            w.write("\par}\n")
        w.write("}\n")
#

if __name__ == "__main__":
    print("Running post gen hook")
    license_file = '{{ cookiecutter.license_file }}'
    if os.path.isfile(license_file):
        with open(license_file) as f:
            l = f.read()
            create_license(l)
    else:
        print("No License file included {}".format(license_file))