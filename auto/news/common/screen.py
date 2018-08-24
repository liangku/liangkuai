import os
def screen_shot(self,address,name):
    img_folder = os.path.abspath(
             os.path.join(os.path.dirname(__file__), "..")) + address
    screen_save_path= img_folder +name + '.png'
    self.driver.get_screenshot_as_file(screen_save_path)