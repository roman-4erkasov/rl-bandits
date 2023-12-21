# rl-bandits
## Данные

Датасет раположен по адресу: http://manikvarma.org/downloads/XC/XMLRepository.html

Статья авторов датасета: https://ivi.fnwi.uva.nl/isis/mediamill/pub/snoek-challenge-acm2006.pdf

В качестве признаков используется 120-мерный вектор, описывающий определенной изображение. И имеется 101 категория, к котороым можно отнести изображения. Нужно определить категории, к которым относятся изображения.


## Результаты
Результаты экспериментов можно посмотреть по ссылке:
https://wandb.ai/roman-4erkasov-signup/rl-bandits-mediamill/reports/Contextual-Online-bandits--Vmlldzo2MzE3OTQ1

В результатах приведены три графика, 2 из которых позволяют сравнить выбранные алгоритмы.


## Выводы
Из результатов эксперменов можно заключить:
- алгоритмы BootsrappedUCB и BootstrappedTS значительно превосходят алгоритм EpsilonGreedy
- Для алгоритмов BootsrappedUCB и BootstrappedTS из рассмотренных гиперпараметров наиболее значимым является nsamples

## Установка
Для установки выполнить команду `make install` & .

## Прменение
Для добавлния описание эксперимента нужно описать конфиг эксперимента в директории [conf/experiment/](conf/experiment/) (Пример конфига [conf/experiment/mediamill_006.yaml](conf/experiment/mediamill_006.yaml))

Для проведения экспеиментов нужно выполнить команду  `venv/bin/python src/main.py -e 7 -e 8 -e 9`. Где 7,8 и 9 это номера экспериментов.
