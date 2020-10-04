import os

contentDir = 'content'
docsDir = 'docs'

pages = [
    {
        "filename": f"{contentDir}/index.html",
        "output": f"{docsDir}/index.html",
        "title": "HIT Blog",
    },
    {
        "filename": f"{contentDir}/about.html",
        "output": f"{docsDir}/about.html",
        "title": "HIT Blog | About",
    },
    {
        "filename": f"{contentDir}/resources.html",
        "output": f"{docsDir}/resources.html",
        "title": "HIT Blog | Resources",
    },

]




def main(pages):


    #merge content with templates
    def mergeTemplate(baseFile, contentFile, title):


        baseFileContent = open(baseFile).read()

        # read the page to a variable
        pageContent = open(contentFile).read()

        # replace contents of base file
        return baseFileContent.replace("{{content}}", pageContent).replace("{{title}}", title)

    #returns basename of the file
    def getBasename(filename):
        return os.path.basename(filename)

    #notify user of file creation
    def fileCreateConfirm(filename):
        print(f'{filename} created successfully!')


    #loop through list of pages
    for page in pages:


        #replace contents of base file
        outputFile = mergeTemplate('templates/base.html', page['filename'], page['title'])

        #get the basename
        fileBasename = getBasename(page['filename'])

        #write to the file
        f = open(f"docs/{fileBasename}", 'w')
        f.write(outputFile)
        f.close()

        #notify user of file creation
        fileCreateConfirm(fileBasename)



main(pages)

