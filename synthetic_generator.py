import os
from tqdm import tqdm
from PIL import Image, ImageEnhance

# Путь к директории с папками synthetic/0, synthetic/1, synthetic/2, ...
dir_path = "images copy"

# Перебираем все поддиректории в директории dir_path
for subdir in tqdm(os.listdir(dir_path)):
    # Проверяем, является ли папка поддиректорией и находится ли в ней файл 0.png
    if os.path.isdir(os.path.join(dir_path, subdir)) and "0.png" in os.listdir(os.path.join(dir_path, subdir)):
        for file in os.listdir(os.path.join(dir_path, subdir)):
            if file != "0.png":
                os.remove(os.path.join(dir_path, subdir, file))
        # Получаем пути к файлам внутри папки
        file_path = os.path.join(dir_path, subdir, "0.png")
        new_file_path = os.path.join(dir_path, subdir, "1.png")
        # Открываем изображение
        image = Image.open(file_path)
        # Увеличиваем яркость на 2%
        enhancer = ImageEnhance.Brightness(image)
        bright_image = enhancer.enhance(1.02)
        # Сохраняем изображение с новым именем
        bright_image.save(new_file_path)
        # Удаляем все файлы, кроме 0.png

