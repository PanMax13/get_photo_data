from exif import Image
from PIL import Image as Img
from PIL.ExifTags import TAGS

class App:
    def __init__(self, path):
        self.path = path

    def help(self): # shows all commands
        pass

    def all_data(self): # get all data from metadata
        image = Img.open(self.path)
        exifdata = image.getexif()
        for tag_id in exifdata:
            tag = TAGS.get(tag_id,tag_id)
            data = exifdata.get(tag_id) 

            if isinstance(data, bytes):
                data = data.decode()

            print(f'{tag:25}: {data}') 


    def meta_coordinates(self): # shows photo coordinates if exist

        with open(self.path, 'rb') as src: # open image 
            self.image = Image(src)

        image_list = self.image.list_all() # get all commands for getting metadata from it

        def dms_coordinates_to_dd_coordinates(coordinates, coordinates_ref): #convert degrees in coordiantes
            decimial_degrees = coordinates[0] + coordinates[1] / 60 +  coordinates[2] / 3600

            if coordinates_ref == 'S' or coordinates_ref == 'W':
                decimial_degrees = -decimial_degrees
            
            return decimial_degrees 

        def show_on_map(): # shows geolocation on map

            latitude = dms_coordinates_to_dd_coordinates(self.image.gps_latitude, self.image.gps_latitude_ref)
            longitude = dms_coordinates_to_dd_coordinates(self.image.gps_longitude, self.image.gps_longitude)
            try: # trying to connect to maps
                import webbrowser 
                
                webbrowser.open(f"https://www.google.com/maps?q={latitude},{longitude}")
            
            except Exception as err: # if error
                return "[!] Something going wrong.... Couldn't to connect to maps...."


        # check if photo include metadata of coordinates, print it and shows in google maps
        # if not, print error message

        if 'gps_latitude' in image_list and 'gps_longitude' in image_list: 
            print(f"Latitude DD : {dms_coordinates_to_dd_coordinates(self.image.gps_latitude, self.image.gps_latitude_ref)}")
            print(f"Latitude DD : {dms_coordinates_to_dd_coordinates(self.image.gps_longitude, self.image.gps_longitude)}")
            show_on_map()
        else: 
            return f"[!] File {self.path} does not include coordinates data"
            

    def camera_data(self): # shows data about camera
        pass

    

app = App('images/jpg/tests/32-lens_data.jpeg')
print(app.all_data())