import subprocess


def launch_game(exe_path: str) -> None:
    try:
        subprocess.Popen([exe_path])
        print(f"Игра успешно запущена.")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
