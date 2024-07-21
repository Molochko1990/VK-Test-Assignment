import subprocess


def import_reg_file(file_path: str) -> None:
    try:
        command = ["REG", "IMPORT", file_path]
        subprocess.run(command, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка выполнения команды: {e.stderr}")
