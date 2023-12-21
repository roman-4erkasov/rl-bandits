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
- Для алгоритмов BootsrappedUCB и BootstrappedTS наиболее значимым параметром является nsamples
- 
