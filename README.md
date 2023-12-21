# rl-bandits

## XOps
Описание экспериментов было максимально перенесено на hydra: описание классов, описание датасетов, описание парсеров, описание условий эксперимента. Установка проводится с помощью Makefile. Эксперименты ведутся с помощью WAndB, используя конфиги в роли иперпараметров.

## Данные

Датасет раположен по адресу: http://manikvarma.org/downloads/XC/XMLRepository.html

Статья авторов датасета: https://ivi.fnwi.uva.nl/isis/mediamill/pub/snoek-challenge-acm2006.pdf

В качестве признаков используется 120-мерный вектор, описывающий определенной изображение. И имеется 101 категория, к котороым можно отнести изображения. Нужно определить категории, к которым относятся изображения.


## Результаты
Результаты экспериментов можно посмотреть по ссылке:
https://api.wandb.ai/links/roman-4erkasov-signup/huiiye2e

В результатах приведены три графика, 2 из которых позволяют сравнить выбранные алгоритмы.


## Выводы
Из результатов эксперменов можно заключить:
- алгоритмы BootsrappedUCB и BootstrappedTS значительно превосходят алгоритм EpsilonGreedy
- Для алгоритмов BootsrappedUCB и BootstrappedTS из рассмотренных гиперпараметров наиболее значимым является nsamples


## Установка
Для установки выполнить команду `make install` .

## Прменение
Для добавлния описание эксперимента нужно описать конфиг эксперимента в директории [conf/experiment/](conf/experiment/) (Пример конфига [conf/experiment/mediamill_006.yaml](conf/experiment/mediamill_006.yaml))

Для проведения экспеиментов нужно выполнить команду  `venv/bin/python src/main.py -e 7 -e 8 -e 9`. Где 7,8 и 9 это номера экспериментов.

## TODO
- Составить конфиги остальных моделей
- Более глубокое изучение гиперпараметров с последующем их варьированием
- Пересмотр выводов после проведения достаточного количества экспериментов

