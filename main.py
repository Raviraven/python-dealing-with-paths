from pathlib import Path, PureWindowsPath
import webbrowser

filename = Path("./test_data.txt")

print(filename.name)
print(filename.suffix)
print(filename.stem)

if not filename.exists():
    print("file doesnt exist")
else:
    print ("file exists")

print("\n{0}\n".format(filename.read_text()))



windowsFilename = PureWindowsPath(".\\text_data.txt")
# below will change path for current OS
correctPath = Path(windowsFilename)
print(correctPath)


webbrowser.open(filename.absolute().as_uri())

print("Program ends here")