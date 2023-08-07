import os
import sys

def readFileContent(file_path):
  with open(file_path, "r") as f:
    content = f.read()
  return content

def createFiles(folder_name):  
  srcFolder = "src/libs"
  libFolder = os.path.join(srcFolder, folder_name)
  if not os.path.exists(libFolder):
    os.makedirs(libFolder)

  fileName = os.path.join(libFolder, folder_name + ".py")
  fileContent = readFileContent("bin/stream/class.txt").replace("<Name>", folder_name.title())
  if not os.path.exists(fileName):
    with open(fileName, "w") as f:
      f.write(fileContent)

  fileNameSchema = os.path.join(libFolder,folder_name+"Schema.py")
  fileContentSchema = readFileContent("bin/stream/schema.txt")
  if not os.path.exists(fileNameSchema):
    with open(fileNameSchema, "w") as f:
      f.write(fileContentSchema)

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("Usage: python lib.play.py <folder_name>")
  else:
    folderName = sys.argv[1]
    createFiles(folderName)

