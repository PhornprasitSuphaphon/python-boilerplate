
import os
import sys
import re
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from src.helpers.converter.camelcase import camelcase
classTemplatePath = "bin/stream/class.txt"
schemaTemplatePath = "bin/stream/schema.txt"

def readFileContent(filePath):
    with open(filePath, "r") as f:
        content = f.read()
    return content

def createFolder(folderPath):
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)

def createPythonFile(filePath, content):
    if not os.path.exists(filePath):
        with open(filePath, "w") as f:
            f.write(content)


def camelcase(s):
  if not any(c.islower() for c in s):
      return s  
  words = re.split(r'[^a-zA-Z0-9]', s)
  camel_case_string = ''.join([word.capitalize() if i != 0 else word for i, word in enumerate(words)])
  return camel_case_string

def main():
    if len(sys.argv) < 1:
        print("Usage: python service.play.py <folder_name>")
    else:
        argvfolderName = sys.argv[1]
        folderName = camelcase(argvfolderName)
        srcFolder = "src/service"
        libFolder = os.path.join(srcFolder, folderName)

        createFolder(libFolder)

        initFilePath = os.path.join(libFolder, "__init__.py")
        createPythonFile(initFilePath, '')

        classFilePath = os.path.join(libFolder, f"{folderName}.py")
        classTemplate = readFileContent(classTemplatePath).replace("<Name>", folderName.title())
        createPythonFile(classFilePath, classTemplate)

        schemaFilePath = os.path.join(libFolder, f"{folderName}Schema.py")
        schemaTemplate = readFileContent(schemaTemplatePath)
        createPythonFile(schemaFilePath, schemaTemplate)

if __name__ == "__main__":
    main()
  
