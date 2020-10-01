import os

def createPage(filename):
    if filename == 'index.html':
        return 'templates/bottom_script.html'
    else:
        return 'templates/bottom.html'




for filename in os.listdir('content'):

    #initialize page_total
    page_total = ''
    #read from top
    page_total += open('templates/top.html').read()
    #read from content
    page_total += open(f'content/{filename}').read()
    #read from bottom
    page_total += open(createPage(filename)).read()

    f = open(f'docs/{filename}', 'w')
    f.write(page_total)
    f.close()




'''
Loop through the files in the directory
Compare the file name with a list of strings
    switch statement     
'''



