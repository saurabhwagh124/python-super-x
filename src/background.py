    

#replace this function with the function in main.py and give parameter to called function eg. self.background("water.jpg").

    def background(self,image_name):    
        # self.image_name= "water.jpg"
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.project_dir = os.path.abspath(os.path.join(self.current_dir, ".."))  # Go up one directory

        self.image_path = os.path.join(self.project_dir,"assets" , image_name)
        oImage = QImage(self.image_path)
        sImage = oImage.scaled(1200,800)

        palette = self.palette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)     




