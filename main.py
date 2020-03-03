from flask import Flask , render_template,request


app = Flask('__main__')

def readTxtFile(filename,startline,endline):
    if len(filename.split('.')) ==2:
        if filename.split('.')[1]=='txt':
            filename = filename
        else:
            print('file required in txt format.')
    else:
        filename +='.txt'

    if (startline is None) or (endline is None):
        if filename == "file2.txt" or filename =="file4.txt":
            with open(filename, 'r', encoding= 'utf-16', errors='ignore') as f:
                filedata = f.readlines()
        else:
            with open(filename, 'r', encoding= 'utf-8', errors='ignore') as f:
                filedata = f.readlines()
    else:
        if filename == "file2.txt" or filename =="file4.txt":
            with open(filename, 'r', encoding= 'utf-16', errors='ignore') as f:
                filedata = f.readlines()
                filedata =filedata[int(startline):int(endline)+1]
        else:
            with open(filename, 'r', encoding= 'utf-8', errors='ignore') as f:
                filedata = f.readlines()
                filedata = filedata[int(startline):int(endline)+1]

    return filedata

@app.route('/',methods =['GET'])
def homePage():
    filename = request.args.get('fname')
    startline = request.args.get('sline')
    endline = request.args.get('eline')
    if filename:
        txtdata = readTxtFile(filename,startline,endline)
    else:
        txtdata = readTxtFile('file1',startline,endline)

    return render_template('home.html', filetxtdata = txtdata)


if __name__ == "__main__":
    app.run(debug=True)
