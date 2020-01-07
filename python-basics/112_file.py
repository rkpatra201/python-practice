%%writefile file.txt
welcome
here agin
type again



#myfile.read() : it reads the file content as string and moves the file pointer to the end of file
#myfile.seek(0) : moves the file pointer to begin of the file.
#content = myfile.read()
#print(content)
# myfile.seek(0)
#print(myfile.read())
#myfile.seek(0)
#myfile.readlines()
#myfile = open(path_to_file)
#myfile.close()
# with opne('myfile.txt') as myfile:
      #content = myfile.read()
# with opne('myfile.txt',mode='r') as myfile:
      #content = myfile.read()
# with opne('myfile.txt',mode='w') as myfile:
      #content = myfile.read() # file not readable error
      # r(read), w(write), a(append), r+ (read and write), w+(write and read)
# with opne('myfile.txt',mode='a') as myfile:
      #myfile.write('welcome')
# with opne('myfile.txt') as myfile:
      #content = myfile.read()