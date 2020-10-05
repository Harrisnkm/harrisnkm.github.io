import os
from jinja2 import Template

'''
Module for creating new pages and merging content with templates
'''

'''Directory Variables'''
contentDir = 'content'
docsDir = 'docs'



def createPagesList():
    '''
    Creates python list of Pages
    '''

    def removeHTMLextension(filename):
        '''
        Removes .html extension from filename input

        :param filename: string with filename.html
        :return: filename without .html extension
        '''

        return filename.replace('.html', '').capitalize()

    def createListItem(filename, title):
        '''
        Creates List object for webpage

        :param filename: filename of webpage
        :param title: Title to be used for webpage
        :return: list object for page
        '''
        return {
            f"filename": f"{contentDir}/{filename}",
            "output": f"{docsDir}/{filename}",
            "title": f"HIT Blog{' | ' + title if filename != 'index.html' else ''}",
            "navLink": f"{filename}",
        }



    # initialize pages list
    pages = []
    # Loops through the content directory
    for filename in os.listdir('content'):
        # remove .html from filename
        pageTitle = removeHTMLextension(filename)

        pages.append(createListItem(filename, pageTitle))

    return pages



def sanitizeNewPage(newFile):
    '''
    Santize input by lowecasing the string and replacing spaces with underscores

    :param newFile: user input for new name of the file
    :return: sanitized input for new file
    '''
    # make newFile lowercase
    newFile = newFile.lower()
    # replace spaces with underscores
    newFile = newFile.replace(' ', '_')

    return newFile

def createNewPage(filename):
    '''
    Adds new page to content directory

    :param filename: filename to be added to content directory
    '''

    #define html content
    newPageHtml = '<h1>New Content!</h1><p>New content...</p>'

    #open a file for writing
    f = open(f'content/{filename}.html', 'w')
    #write to the file
    f.write(newPageHtml)
    #close the file
    f.close()




def main():



    # returns basename of the file
    def getBasename(filename):
        '''
        Get basename of the file

        :param filename: file with path
        :return: base name of the file
        '''
        return os.path.basename(filename)

    # notify user of file creation
    def fileCreateConfirm(filename):
        '''
        Outputs to user confirmation of file creation

        :param filename: filename that was created
        '''
        print(f'{filename} created successfully!')

    # merge content with templates
    def mergeTemplate(baseFile, contentFile, title):
        '''
        Uses Jinja to merge content file with template file

        :param baseFile: base.html
        :param contentFile: files in /content/ to be merged
        :param title: Title of the page
        :return: returned the merged template
        '''
        baseFileContent = open(baseFile).read()

        # read the page to a variable
        pageContent = open(contentFile).read()

        # return rendered template
        template = Template(baseFileContent)
        return template.render(
            title=title,
            content=pageContent,
            pages=pagesList,
        )



    #create pagesList
    pagesList = createPagesList()

    #loop through list of pages
    for page in pagesList:


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

