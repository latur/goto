#  GoTo Camp 2016

## Ссылки

 * Таблица аминокислот [здесь](https://github.com/latur/Bioinformatics/blob/master/%40bio.js#L114)
 * Множественные выравнивания [ClustalW / ClustalX](http://www.clustal.org/clustal2/)
 * Сеть генных взаимодействий [HumanNet](http://www.functionalnet.org/humannet/download.html)


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

Задача на машинное обучение. Есть обучающая `X1/test.fa` и тестовая `X1/train.fa` выборка. Индикатор класса — перавя буква в названии рида. Нужно построить классификатор и каждому риду из тестовой выборки присвоить свой индикатор. Индикаторы в том же порядке что и риды записать в файл и загрузить в проверяющую систему. Использовать можно всё что угодно (кроме брута проверяющей системы).

[dev.mazepa.us/goto/x1.php](http://dev.mazepa.us/goto/x1.php)

