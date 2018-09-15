import os
class RenamingFiles :
    def list_files(self , folder_direction):
        self.folder_path = folder_direction
        try:
            self.files = os.listdir(self.folder_path)
            self.extension = self.files[0].split('.')[1]
            print("the files in directory : ",self.folder_path)
            print("the folder files : ", self.files)
            print('the files extension :' , self.extension)
        except:
            raise ValueError('the foldet path must be in this format : folder \\ folder \\folder ')

    def chaning_name(self,new_name,start_number = 0):
        try:
            for file in self.files:
                pic_path = os.path.join(self.folder_path, file)
                os.rename(pic_path, self.folder_path + '\\'+str(new_name) + str(start_number) + '.'+self.extension)
                start_number += 1
            print('changing names is DONE ')
        except: raise ValueError('the files dosent have the same extension or the files have the same name')


