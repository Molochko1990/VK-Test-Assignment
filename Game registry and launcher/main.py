import sys
import os

from utils.find_game_path import GamePathFinder
from utils.file_downloader import FileDownloader
from utils.reg_parser import import_reg_file
from utils.game_launcher import launch_game
from settings import GAME_NAME, DOWNLOAD_URL, ROOT_FOLDERS, FILENAME


def main():
    executable_name = GAME_NAME

    finder = GamePathFinder(executable_name, ROOT_FOLDERS)
    game_path = finder.find_game_path()

    if game_path:
        print(f"Игра найдена в: {game_path}")
    else:
        print("Игра не найдена")
        sys.exit("Убедитесь, что игра скачана и ее имя в файле settings указано корректно")

    downloader = FileDownloader(game_path, FILENAME)

    try:
        downloader.download_from_google_drive(DOWNLOAD_URL)
    except Exception as e:
        print(f"Произошла ошибка при скачивании файла: {e}")
        sys.exit()

    reg_file_path = os.path.join(downloader.get_save_dir(), FILENAME)
    import_reg_file(reg_file_path)

    game_exe = os.path.join(game_path, GAME_NAME)
    launch_game(game_exe)


if __name__ == "__main__":
    main()
