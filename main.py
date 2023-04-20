from exif import Image


class App:
    def __init__(self, path):
        self.path = path

    def open_img(self):
        with open(path, 'rb') as src:
            self.image = src.read()
        
            print('opened')

    def help(self): # shows all commands
        open_img() #NameError: name 'open_img' is not defined

    def all_data(self): # shows all photo's metadata
        pass

    def meta_coordinates(self): # shows coordinates from metadata
        pass

    def camera_data(self): # shows data about camera
        pass

    

app = App('images/jpg/Canon_40D_photoshop_import.jpg')
app.help()