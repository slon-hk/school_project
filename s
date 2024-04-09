[33mcommit e715dbd68dd9517005d199fc931eb57faa8f8494[m[33m ([m[1;36mHEAD -> [m[1;32mmain[m[33m)[m
Author: slon_hk <st3panov.len@yandex.ru>
Date:   Tue Apr 2 21:27:43 2024 +0300

    Update readme file

[1mdiff --git a/README.md b/README.md[m
[1mindex de0e428..5548c11 100644[m
[1m--- a/README.md[m
[1m+++ b/README.md[m
[36m@@ -1,4 +1,4 @@[m
[31m-<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="__0"></a>Математические модели</h1>[m
[32m+[m[32m﻿<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="__0"></a>Математические модели</h1>[m
 <p class="has-line-data" data-line-start="3" data-line-end="4">Проект “математические модели” открывает перед пользователями новые возможности для практического применения математики в реальном мире. Созданная программа способствует более глубокому пониманию математических концепций и их влияния на окружающую среду. Этот проект призван вдохновить людей использовать математику как мощный инструмент для решения реальных задач и привнести новый взгляд на то, как математика может быть полезна в повседневной жизни.</p>[m
 <h2 class="code-line" data-line-start=5 data-line-end=6 ><a id="_5"></a>Проблема</h2>[m
 <p class="has-line-data" data-line-start="6" data-line-end="7">Cложность вычисления и построение наглядных математических моделей, построение их в пространстве.</p>[m
[1mdiff --git a/main.py b/main.py[m
[1mindex ea9c839..a3efa04 100644[m
[1m--- a/main.py[m
[1m+++ b/main.py[m
[36m@@ -66,11 +66,16 @@[m [mclass MyTabView(ctk.CTkTabview):[m
     def __init__(self, master, **kwargs):[m
         super().__init__(master, **kwargs)[m
 [m
[31m-        # РЎРѓР С•Р В·Р Т‘Р В°Р Р…Р С‘Р Вµ Р Р†Р С”Р В»Р В°Р Т‘Р С•Р С”[m
[32m+[m[32m        # Созжание вкладок[m
         self.add("Функции")[m
         self.add("Инструкция")[m
 [m
[31m-        # Р Т‘Р С•Р В±Р В°Р Р†Р В»Р ВµР Р…Р С‘Р Вµ Р Р†Р С‘Р Т‘Р В¶Р ВµРЎвЂљР С•Р Р† Р Р…Р В° Р Р†Р С”Р В»Р В°Р Т‘Р С”Р С‘[m
[32m+[m[32m        # Создания поля ввода[m
[32m+[m[32m        intro_text = "Тык Тык Тык\n тык тык тык\n тык тык тык"[m
[32m+[m[32m        self.intro_text = ctk.CTkLabel(master = self.tab("Функции"), text=intro_text)[m
[32m+[m[32m        self.intro_text.grid([m
[32m+[m[32m            row=0, column=1, padx=5, pady=10, sticky="ew", columnspan=2[m
[32m+[m[32m        )[m
         self.pole_vvoda = ctk.CTkEntry([m
             master=self.tab("Функции"),[m
             height=50,[m
[36m@@ -78,14 +83,21 @@[m [mclass MyTabView(ctk.CTkTabview):[m
             placeholder_text="Введите текст",[m
         )[m
         self.pole_vvoda.grid([m
[31m-            row=1, column=1, padx=5, pady=10, sticky="ew", columnspan=2[m
[32m+[m[32m            row=2, column=1, padx=5, pady=10, sticky="ew", columnspan=2[m
         )[m
 [m
         # slider[m
[32m+[m[32m        label_slider_text = "Установка точности построения графика"[m
[32m+[m[32m        self.label_slider = ctk.CTkLabel([m
[32m+[m[32m            master=self.tab("Функции"), text=label_slider_text[m
[32m+[m[32m        )[m
[32m+[m[32m        self.label_slider.grid([m
[32m+[m[32m            row=3, column=1, padx=5, pady=10, sticky="ew", columnspan=2[m
[32m+[m[32m        )[m
         self.slider = ctk.CTkSlider([m
             master=self.tab("Функции"), height=30, width=740, from_=1, to=0.01[m
         )[m
[31m-        self.slider.grid(row=2, column=1, padx=5, pady=10, sticky="ew", columnspan=2)[m
[32m+[m[32m        self.slider.grid(row=4, column=1, padx=5, pady=10, sticky="ew", columnspan=2)[m
 [m
         # enter button[m
         self.button = ctk.CTkButton([m
[36m@@ -95,7 +107,7 @@[m [mclass MyTabView(ctk.CTkTabview):[m
             width=360,[m
             height=50,[m
         )[m
[31m-        self.button.grid(row=3, column=1, padx=5, pady=10)[m
[32m+[m[32m        self.button.grid(row=5, column=1, padx=5, pady=10)[m
 [m
         self.clear_button = ctk.CTkButton([m
             master=self.tab("Функции"),[m
[36m@@ -104,7 +116,7 @@[m [mclass MyTabView(ctk.CTkTabview):[m
             width=360,[m
             height=50,[m
         )[m
[31m-        self.clear_button.grid(row=3, column=2, padx=5, pady=10)[m
[32m+[m[32m        self.clear_button.grid(row=5, column=2, padx=5, pady=10)[m
 [m
         # TAB 2[m
         self.my_frame = MyFrame(master=self.tab("Инструкция"), width=700, height=400)[m

[33mcommit da731f71670b27b59383d4295ec35a7f9516fc2f[m[33m ([m[1;31morigin/main[m[33m, [m[1;31morigin/HEAD[m[33m)[m
Author: slon_hk <st3panov.len@yandex.ru>
Date:   Tue Apr 2 00:07:40 2024 +0300

    Update readme file

[1mdiff --git a/README.md b/README.md[m
[1mindex 1006b4c..de0e428 100644[m
[1m--- a/README.md[m
[1m+++ b/README.md[m
[36m@@ -13,6 +13,7 @@[m
 <h2 class="code-line" data-line-start=19 data-line-end=20 ><a id="_19"></a>Аннотация</h2>[m
 <p class="has-line-data" data-line-start="20" data-line-end="21">Продуктом проектной деятельности является программа, предназначенная для создания математических моделей в трехмерном и двумерном пространстве.</p>[m
 <h2 class="code-line" data-line-start=22 data-line-end=23 ><a id="_22"></a>Примеры использования программы</h2>[m
[32m+[m[32m<p class="has-line-data" data-line-start="23" data-line-end="24"><img src="\image\gif_1.gif" alt="App Screenshot"></p>[m
 <p class="has-line-data" data-line-start="23" data-line-end="24"><img src="\image\image_1.jpg" alt="App Screenshot"></p>[m
 <p class="has-line-data" data-line-start="23" data-line-end="24"><img src="\image\image_2.jpg" alt="App Screenshot"></p>[m
 <p class="has-line-data" data-line-start="23" data-line-end="24"><img src="\image\image_3.jpg" alt="App Screenshot"></p>[m
[1mdiff --git a/image/gif_1.gif b/image/gif_1.gif[m
[1mnew file mode 100644[m
[1mindex 0000000..e75c76b[m
Binary files /dev/null and b/image/gif_1.gif differ
[1mdiff --git a/main.py b/main.py[m
[1mindex a814fee..ea9c839 100644[m
[1m--- a/main.py[m
[1m+++ b/main.py[m
[36m@@ -4,6 +4,7 @@[m [mimport tkinter as tk[m
 from tkinter import ttk[m
 from PIL import ImageTk, Image[m
 [m
[32m+[m[32mfrom math import *[m
 import sympy as sp[m
 import numpy as np[m
 import matplotlib.pyplot as plt[m

[33mcommit 467c69125bb835bb0e8e88b68a3b65102ac8a97e[m
Author: slon_hk <st3panov.len@yandex.ru>
Date:   Mon Apr 1 23:53:41 2024 +0300

    Update readme file

[1mdiff --git a/README.md b/README.md[m
[1mindex aec830b..1006b4c 100644[m
[1m--- a/README.md[m
[1m+++ b/README.md[m
[36m@@ -25,6 +25,7 @@[m
 <p class="has-line-data" data-line-start="23" data-line-end="24"><img src="\image\image_9.jpg" alt="App Screenshot"></p>[m
 <h2 class="code-line" data-line-start=22 data-line-end=23 ><a id="_22"></a>Необходимые модули</h2>[m
 <p class="has-line-data" data-line-start="20" data-line-end="19">При необходимости используйте pip3:[m
[32m+[m
         pip install sympy[m
 [m
         pip install numpy[m

[33mcommit 936eb31c4ab5a8232adf22bd044d7dbb691aa6fc[m
Author: s