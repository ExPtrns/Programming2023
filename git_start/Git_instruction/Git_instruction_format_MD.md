# Инструкция по работе с Git в формате MD
## 1. Основные команды в Git:
* git init - cоздание репозитория в существующем каталоге;
* git add 'имя файла' - добавляет файл для отслеживания изменений;
* git commit -m "'Описание произведенного изменения'"
* git status - показывает измененные файлы, которые были изменены и либо не добавлены для отслеживание, либо ожидают commit;
* git log - вызывает список всех действий и сохранений (ключ --graph - отображает commits в виде дерева);
* git diff 'имя сохраненной версии файла' - показывает разницу между версиями (в имени достаточно написать 5 первых символов версии);
* git chechout - позволяет переключиться между разными версиями файла или ветками;
* clear - очищает экран терминала;
* git branch 'имя ветки' - создает новую ветку файла (черновик) с указанным именем, паралельно основной (master);
* git branch - выводит на экран список веток (активная ветка помечена знаком '*');
* git merge 'имя ветки' - делает слияние изменений из указанной ветки в текущую;
* git branch -d 'имя ветки' - удаляет указанную ветку.
* git clone 'полный адрес удаленного репозитория' - копирует репозиторий с удаленного источника в текущий каталог;
* git push 'полный адрес удаленного репозитория' - загружает изменения c локального репозитория на удаленный репозиторий;
* git pull 'полный адрес удаленного репозитория' - загружает изменения c удаленного репозитория на локальный репозиторий;

## 2. Выделение текста в формате MD
Для видоизменения отображаемого текста используются специальные символы:
* '*' - с обеих сторон - текст выводится курсивом   - *Пример текста*;
* '**' - с обеих сторон - полужирный текст  - **Пример текста**;
* '#' - перед текстом - указать заголовок или '##' - подзаголовок;
* '~~' - с обеих сторон - зачеркнутый текст - ~~Пример текста~~.

## 3. Списки
Для добаления ненумерованного списка используется знак '* ' в начале строки. Пример:
* Элемент 1;
* Элемент 2;
* Элемент 3.

Для добавления нумерованного списка - нумеруем цифрами каждый пункт. Пример:

1. Элемент 1;
1. Элемент 2;
1. Элемент 3.


## 4. Работа с изображениями
Для добавления изображения необходимо использовать команду '![Описание изображения](/Имя файла)'.
Например:
![Логотип MD](markdown.png)
## 5. Ссылки
Для добавления ссылки в формате MD используется команда '[Название ссылки](Адрес ссылки)'.
Пример [Поисковик гугл](https://www.google.com/)
## 6. Работа с таблицами
Для компактного отображения информации в формате MD можно использовать таблицы.
Для этого необходимо поместить пункт таблицы между символами '|', для разделения
заголовка от основной таблицы используем '|-|'.
Пример

| Заголовок 1 | Заголовок 2 | Заголовок 3 | Заголовок 4 |
|-|-|-|-|
|Ячейка 1|Ячейка 2|Ячейка 3|Ячейка 4|


## 7. Цитаты
Для цитирования текста достаточно поместить его после символа > - первый уровень
цитирования >> - второй уровень цитирования и >>> - третий уровень цитирования
Пример
> Цитата 1 уровня
>> Цитата 2 уровня
>>> Цитата 3 уровня
## 8. Заключение
В таблице инструкции только основные команды для работы в формате MarkDown.
При необходимости информацию можно расширить.
