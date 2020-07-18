# Без масочки не обслуживаем

### Пожалуйста, любое изменение master делать через Pull Request!

###### По фото или видео определить, есть ли на человеке медицинская маска или нет. Усложнение: использовать видео с камеры, имитирующей камеру видеонаблюдения. Усложнение Х2: посчитать количество людей в маске и без по видео с общим планом

[![Build Status](https://travis-ci.com/SinM9/no_service_without_masks.svg?branch=master)](https://travis-ci.com/SinM9/no_service_without_masks)

### Создание нового модуля (Python)

- В каталоге `modules` создайте папку в формате `[0-9]_any_name`. Пример: `1_sourse`.
- Зайдите во вновь созданную папку, там должно быть, как минимум, 2 файла (реализация и тесты).
  - `any_name.py` ваша реализация. Пример `sourse.py`.
  - `test_folderName.py` тесты к вашей реализации. Должны иметь то же имя, что и папка и начинаться с `test_`. Пример: `test_sourse.py`  

### Общие правила

- Для тестирования используется модуль `unittest`, как писать тесты можно прочитать [здесь](https://docs.python.org/3/library/unittest.html), или посмотреть в примере`test_sourse.py`.
- Изображения, `.xml`,`.bin`, файлы загружать в `data`, для доступа к ним использовать модуль `os` ([Информация](https://docs.python.org/3/library/os.path.html#module-os.path))
- Прежде чем залить новый модуль на Git, нужно изменить файл`travis.yml` в корневой директории, а точнее добавить скрипт запускающий ваш файл с тестами. После строки `# add new modules here` вставить `- python3 -m unittest -v test_name`, где `test_name` имя вашего теста.

### Настройка окружения для локального тестирования

#### Linux

```
export PYTHONPATH=$(ls modules | xargs -I {} sh -c 'printf $(pwd)/modules/{}:')$PYTHONPATH
mkdir build && cd build
source /opt/intel/openvino/bin/setupvars.sh
cmake -DCMAKE_BUILD_TYPE=Release .. && make -j4
python3 -m unittest -v test_name #Запуск тестов, где test_name имя вашего теста
```

### Визуализация

<img src="data/conference.png" width="256" title="before"> <img src="data/out.png" width="256" title="after">
