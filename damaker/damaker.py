from processing import *

def app():
    help_str = """
        DAMAKER commands info:
            - open "file" : load a .tiff file to work on.
            - save "file" : save the current work to a file.
            - plot : display the current stack of image.
            - invert : invert the color on each grayscale frame.
            - crop x1 y1 x2 y2 : cut the frame stack on the given coordinates.
            - quit | q : stop the program.
    """
    print(help_str)
    
    tiff = TiffObject("")
    
    stop = False
    while not stop:
        inp = input(tiff.name + ">")
        args = inp.split(" ")
        if inp.startswith("open"):
            if len(args) > 1:
                tiff = openTiff(args[1])
                if tiff is list:
                    tiff = tiff[0]
            else:
                print("[DAMAKER] Warning: no filename in argument")
        elif inp.startswith("save"):
            if len(args) > 1:
                tiff.save(args[1])
            else:
                print("[DAMAKER] Warning: no filename in argument")
        elif inp.startswith("plot"):
            plot(tiff)
        elif inp.startswith("invert"):
            tiff.invert()
        elif inp.startswith("crop"):
            if len(args) > 4:
                crop(tiff, (int(args[1]), int(args[2])), (int(args[3]), int(args[4])))
            else:
                print("[DAMAKER] Warning: not enough arguments")
        elif inp.startswith("quit") or inp == "q":
            stop = True

if __name__ == '__main__':
    app()