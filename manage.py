import sys
import utils


if len(sys.argv) < 2:
    print("Please specify 'build' or 'new'")

else:
    command = sys.argv[1]

    if command == "build":
        utils.main()
    elif command == "new":
        #ask user for input
        newFile = input('Name the new file: ')
        newFile = utils.sanitizeNewPage(newFile)
        utils.createNewPage(newFile)
    else:
        print("Please specify 'build' or 'new'")


