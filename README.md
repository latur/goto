#  GoTo Camp 2016

## Неслучайность генома

Формат `.fasta` — текстовый формат для хранения аминокислотных или нуклеотиндных последовательностей Содержит название, начинающееся с символа `>` и саму последовательность после символа конца строки `\n`. При этом в ней допускаются переносы строк. Пример:

~~~
>MCHU - Calmodulin - Human
ADQLTEEQIAEFKEAFSLFDKDGDGTITTKE
DIDGDGQVNYEEFVQMMTAK*
>gi|5524211|gb|AAD44166.1| cytochrome b
LCLYTHIGRNIYYGSYLYSETWNTGIMLLLI
LLILILLLLLLALLSPDMLGDPDNHMPADPL
NTPLHIKPEWYFLFAYAILRSVPNKLGGVLA
IENY
~~~

### Задание:

Задача на машинное обучение. Есть обучающая `data/X1/test.fa` и тестовая `data/X1/train.fa` выборка. Индикатор класса — первая буква в названии рида. Нужно построить классификатор и каждому риду из тестовой выборки присвоить свой индикатор. Индикаторы в том же порядке что и риды записать в файл и загрузить в проверяющую систему. Использовать можно всё что угодно

[dev.mazepa.us/goto/x1.php](http://dev.mazepa.us/goto/x1.php)

## Выравнивания и множественные выравнивания

### Задание:

В папке `data/X2/reads.fa.zip` лежат уже выровненные риды. Используя полученные знания о процессе мутации и отбора локализовать сайты сплайсига. Аккуратно, степень выполнимости задачи неизвестна.

[dev.mazepa.us/goto/x2.php](http://dev.mazepa.us/goto/x2.php)

## Ссылки

 * Множественные выравнивания [ClustalW / ClustalX](http://www.clustal.org/clustal2/)
 * Сеть генных взаимодействий [HumanNet](http://www.functionalnet.org/humannet/download.html)
 * JS [библиотечка](https://github.com/latur/Bioinformatics) и [список аминокислот](https://github.com/latur/Bioinformatics/blob/master/%40bio.js#L114)
