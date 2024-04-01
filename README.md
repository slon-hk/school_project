<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="__0"></a>Математические модели</h1>
<p class="has-line-data" data-line-start="3" data-line-end="4">Проект “математические модели” открывает перед пользователями новые возможности для практического применения математики в реальном мире. Созданная программа способствует более глубокому пониманию математических концепций и их влияния на окружающую среду. Этот проект призван вдохновить людей использовать математику как мощный инструмент для решения реальных задач и привнести новый взгляд на то, как математика может быть полезна в повседневной жизни.</p>
<h2 class="code-line" data-line-start=5 data-line-end=6 ><a id="_5"></a>Проблема</h2>
<p class="has-line-data" data-line-start="6" data-line-end="7">Cложность вычисления и построение наглядных математических моделей, построение их в пространстве.</p>
<h2 class="code-line" data-line-start=8 data-line-end=9 ><a id="__8"></a>Цель проекта</h2>
<p class="has-line-data" data-line-start="9" data-line-end="10">Предоставление ученикам интуитивно понятного программного средства для создания и анализа математических моделей в трехмерном пространстве.</p>
<h2 class="code-line" data-line-start=11 data-line-end=12 ><a id="__11"></a>Тип проекта</h2>
<p class="has-line-data" data-line-start="12" data-line-end="13">Практико-ориентированный</p>
<h2 class="code-line" data-line-start=14 data-line-end=15 ><a id="_14"></a>Задачи</h2>
<p class="has-line-data" data-line-start="15" data-line-end="18">•   Изучение библиотек для создания графического интерфейса.<br>
•   Изучение библиотек для построения и вычисления математических моделей.<br>
•   Простой и интуитивно понятный интерфейс для создания математических моделей в трехмерном и двумерном пространстве.</p>
<h2 class="code-line" data-line-start=19 data-line-end=20 ><a id="_19"></a>Аннотация</h2>
<p class="has-line-data" data-line-start="20" data-line-end="21">Продуктом проектной деятельности является программа, предназначенная для создания математических моделей в трехмерном и двумерном пространстве.</p>
<h2 class="code-line" data-line-start=22 data-line-end=23 ><a id="_22"></a>Примеры использования программы</h2>
<p class="has-line-data" data-line-start="23" data-line-end="24"><img src="\image\image_1.jpg" alt="App Screenshot"></p>
<p class="has-line-data" data-line-start="23" data-line-end="24"><img src="\image\image_2.jpg" alt="App Screenshot"></p>
<p class="has-line-data" data-line-start="23" data-line-end="24"><img src="\image\image_3.jpg" alt="App Screenshot"></p>
<p class="has-line-data" data-line-start="23" data-line-end="24"><img src="\image\image_5.jpg" alt="App Screenshot"></p>
<p class="has-line-data" data-line-start="23" data-line-end="24"><img src="\image\image_6.jpg" alt="App Screenshot"></p>
<p class="has-line-data" data-line-start="23" data-line-end="24"><img src="\image\image_7.jpg" alt="App Screenshot"></p>
<p class="has-line-data" data-line-start="23" data-line-end="24"><img src="\image\image_8.jpg" alt="App Screenshot"></p>
<h2 class="code-line" data-line-start=22 data-line-end=23 ><a id="_22"></a>Интерфейс программы</h2>
<p class="has-line-data" data-line-start="23" data-line-end="24"><img src="\image\image_4.jpg" alt="App Screenshot"></p>
<p class="has-line-data" data-line-start="23" data-line-end="24"><img src="\image\image_9.jpg" alt="App Screenshot"></p>
<h2 class="code-line" data-line-start=22 data-line-end=23 ><a id="_22"></a>Необходимые модули</h2>
<p class="has-line-data" data-line-start="20" data-line-end="21">При необходимости используйте pip3
        pip install sympy
        pip install numpy
        pip install matplotlib
        pip install mpl-toolkits.clifford
        pip install matplotlib
        pip install customtkinter
        pip install tkinter</p>
<h2 class="code-line" data-line-start=22 data-line-end=23 ><a id="_22"></a>Инструкция</h2>
<p class="code-line" data-line-start=19 data-line-end=20 ><a id="_19"></a>Данная программа предназначена для построения моделей в пространстве. Ниже приведены все математические функции которые поддерживаются программой:

        Сложение двух чисел - x+n

        Вычитание двух чисел - x-n

        Умножение - x*n

        Деление двух чисел - x/n

        Целочисленное деление двух чисел - x//n

        Получение остатка от деления - x%n

        Возведение в степень - x**n

        fabs(X) - модуль X.

        factorial(X) - факториал числа X.

        floor(X) - округление вниз.

        fmod(X, Y) - остаток от деления X на Y.

        frexp(X) - возвращает мантиссу и экспоненту числа.

        ldexp(X, I) - X * 2I. Функция, обратная функции math.frexp().

        fsum(последовательность) - сумма всех членов последовательности. Эквивалент встроенной функции sum(), но math.fsum() более точна для чисел с плавающей точкой.

        modf(X) - возвращает дробную и целую часть числа X. Оба числа имеют тот же знак, что и X.

        trunc(X) - усекает значение X до целого.

        exp(X) - eX.

        log(X, [base]) - логарифм X по основанию base. Если base не указан, вычисляется натуральный логарифм.

        log1p(X) - натуральный логарифм (1 + X). При X → 0 точнее, чем math.log(1+X).

        log10(X) - логарифм X по основанию 10.

        log2(X) - логарифм X по основанию 2.

        pow(X, Y) - XY.

        sqrt(X) - квадратный корень из X.

        acos(X) - арккосинус X. В радианах.

        asin(X) - арксинус X. В радианах.

        atan(X) - арктангенс X. В радианах.

        atan2(Y, X) - арктангенс Y/X. В радианах. С учетом четверти, в которой находится точка (X, Y).

        cos(X) - косинус X (X указывается в радианах).

        sin(X) - синус X (X указывается в радианах).

        tan(X) - тангенс X (X указывается в радианах).

        degrees(X) - конвертирует радианы в градусы.

        radians(X) - конвертирует градусы в радианы.

        cosh(X) - вычисляет гиперболический косинус.

        sinh(X) - вычисляет гиперболический синус.

        tanh(X) - вычисляет гиперболический тангенс.

        acosh(X) - вычисляет обратный гиперболический косинус.

        asinh(X) - вычисляет обратный гиперболический синус.

        atanh(X) - вычисляет обратный гиперболический тангенс.

        gamma(X) - гамма-функция X.

        lgamma(X) - натуральный логарифм гамма-функции X.

        pi - pi = 3,1415926...

        e - e = 2,718281...

        Более подробный список функций вы можете найти в документации встроенной библиотеки\n\n        python - math, numpy и matplotlib
		</p>