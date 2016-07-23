#  GoTo Camp 2016


## Ссылки

### Инструменты

 * Множественные выравнивания [ClustalW / ClustalX](http://www.clustal.org/clustal2/)
 * Сеть генных взаимодействий [HumanNet](http://www.functionalnet.org/humannet/download.html)
 * JS [библиотечка](https://github.com/latur/Bioinformatics) и [список аминокислот](https://github.com/latur/Bioinformatics/blob/master/%40bio.js#L114)

### Учёба

 * [Rosalind. Bioinformatics Armory](http://rosalind.info/problems/tree-view/?location=bioinformatics-armory)
 * [Stepik. Молекулярная биология и генетика](https://stepic.org/course/%D0%9C%D0%BE%D0%BB%D0%B5%D0%BA%D1%83%D0%BB%D1%8F%D1%80%D0%BD%D0%B0%D1%8F-%D0%B1%D0%B8%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%8F-%D0%B8-%D0%B3%D0%B5%D0%BD%D0%B5%D1%82%D0%B8%D0%BA%D0%B0-70/)
 * [Stepik. Биотехнологии: генная инженерия](https://stepic.org/course/%D0%91%D0%B8%D0%BE%D1%82%D0%B5%D1%85%D0%BD%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D0%B8-%D0%B3%D0%B5%D0%BD%D0%BD%D0%B0%D1%8F-%D0%B8%D0%BD%D0%B6%D0%B5%D0%BD%D0%B5%D1%80%D0%B8%D1%8F-94/)


## Задания

### Неслучайность генома

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

#### Задание:

Задача на машинное обучение. Есть обучающая `data/X1/test.fa` и тестовая `data/X1/train.fa` выборка. Индикатор класса — первая буква в названии рида. Нужно построить классификатор и каждому риду из тестовой выборки присвоить свой индикатор. Индикаторы в том же порядке что и риды записать в файл и загрузить в проверяющую систему. Использовать можно всё что угодно

[dev.mazepa.us/goto/x1.php](http://dev.mazepa.us/goto/x1.php)


### Выравнивания и множественные выравнивания

#### Задание:

В папке `data/X2/reads.fa.zip` лежат уже выровненные риды. Используя полученные знания о процессе мутации и отбора локализовать сайты сплайсига. Аккуратно, степень выполнимости задачи неизвестна.

[dev.mazepa.us/goto/x2.php](http://dev.mazepa.us/goto/x2.php)

#### Подсказка:

```
MEGVGGLWPWVLGLLSLPGVILGAPLASSCPGACDTSFPDGLTPEGTQASG
DKDIPAINQGLIPEETPESSFLIEGDIVRPSPFRLLSATSNKWPTGGGGVV
EVPFLLSSKYDEPSRQVILEALAEFEHSTCVRFVPYEGQRDFISIIPMYGC
FSSVGRSGGMQVVSLAPTCLQKGRGIVLHELMHVLGFWHEHARADRDRYIR
VNWNEILPGFEINFIKSRSSNMLTPYDYSSVMHYGRLAFSRRGLPTITPLW
APSVHIGQRWNLSASDITRVLKLYGCSPSGPSPVGEGSHAHSTDRSPAPAS
LSLQQLLEALSAESTSPDLIGSSALGQPAPAGPGESPPGWESPALKKLSAE
ASARQPQTLASSPRSRPGAGAPGVAQEQSWLAGVSTEPTVPSSEAGIQPVP
VQGSPALPGGCVPGNHFKGRSKD
```
