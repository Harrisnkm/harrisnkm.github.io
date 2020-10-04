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



    def mergeTemplate(baseFile, contentFile, title):


        baseFileContent = open(baseFile).read()

        # read the page to a variable
        pageContent = open(contentFile).read()

        # replace contents of base file
        return baseFileContent.replace("{{content}}", pageContent).replace("{{title}}", title)



    #loop through list of pages
    for page in pages:


        #replace contents of base file
        output_file = mergeTemplate('templates/base.html', page['filename'], page['title'])

        #write to the file
        f = open(f"docs/{os.path.basename(page['filename'])}", 'w')
        f.write(output_file)
        f.close()





main(pages)

