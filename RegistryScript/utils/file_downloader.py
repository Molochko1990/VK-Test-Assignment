import os
import gdown


class FileDownloader:
    def __init__(self, save_dir: str, filename: str) -> None:
        self._save_dir = save_dir
        self._filename = filename

    def download_from_google_drive(self, url: str) -> None:
        try:
            output_path = os.path.join(self._save_dir, self._filename)
            gdown.download(url, output_path, quiet=False)
            print(f"Файл успешно скачан и сохранен в {output_path}")
        except Exception as e:
            print(f"Произошла ошибка при скачивании файла: {str(e)}")

    def get_save_dir(self):
        return self._save_dir
