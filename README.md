# vmestecdn_python

Видеохостинг для загрузки своего онлайн-видео

## Где найти токен

Токен можно найти на странице профиля в видеохостинге

## Функции
### Подключение
```python
from vmestecdn_upload import VmestecdnUpload
```
### Загрузка видео
```python
vcu = VmestecdnUpload("your_token") # токен из вашего личного кабинета
# загрузить свой файл
uuid = vcu.upload_file("/path/to/file.avi") # вернется идентификатор загруженного файла
```
### Получение информации
```python
vcu.info(uuid) # вернется ответ в формате json с информацией о файле
```
### Удаление 
```python
vcu.delete(uuid) # вернется ответ в формате json с результатом удаления и текстом ошибки, если status: failure
```
