import os

class Create:
    def __init__(self, dirs:list):
        self.dirs = dirs

    def make_dirs(self, dir):
        for d in self.dirs:
            os.makedirs(f"{dir}/{d}")

    def make_base_files(self, dir:str, ext:str):
        with open(f"{dir}/.gitignore", 'w') as f:
            f.write("Write your files to ignore in commits here.")
            f.close()
        
        with open(f"{dir}/main.{ext}", 'w') as f:
            f.write("'Begin Writing code! Star me on GitHub if you found this tool helpful <3'")
            f.close()

        with open(f"{dir}/readme.md", 'w') as f:
            f.write("## Welcome to my super cool project!\nThese are my project details!")
            f.close()