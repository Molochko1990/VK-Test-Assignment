import os


class GamePathFinder:
    def __init__(self, executable_name, root_folders):
        self.executable_name = executable_name
        self.root_folders = root_folders

    def find_game_path(self):
        for root_folder in self.root_folders:
            print(f"Поиск в {root_folder}...")
            for root, dirs, files in os.walk(root_folder):
                for file in files:
                    if self.executable_name.lower() in file.lower():
                        return os.path.join(root)
        return None


