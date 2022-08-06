# Least squares for programmers with illustrations 程序员的最小二乘法可视化教程

本仓库是[SIGGRAPH 2021 课程](https://github.com/ssloy/least-squares-course)的个人翻译。

原作者：[Dmitry Sokolov](https://members.loria.fr/DSokolov/)，[Nicolas Ray](https://members.loria.fr/NRay/)，[Etienne Corman](https://members.loria.fr/ECorman/)

课程源码：[source code](https://github.com/ssloy/least-squares-course/tree/master/src)

课程视频：[![](https://raw.githubusercontent.com/ssloy/least-squares-course/master/presentation/screenshot.jpg)](https://youtu.be/ZDh3v8OAEIA)


本课程介绍一种简单易学的技术：最小二乘优化。我们会展示这种简单的方法如何解决大量其他方法难以驾驭的问题。本课程提供了一套简单、易于理解的强大工具，大多数程序员可以轻松上手。与此相对，其他采用最小二乘范式的复杂算法（如数值模拟、深度学习）更难掌握。

线性回归（Linear regression）通常被低估为统计学或数据分析的一个子领域，但它的内涵远不止于此。我们会挖掘用同样的方法（最小二乘）来操作几何体。进入数值优化世界的第一步并不需要很强的应用数学背景。迈出的第一步虽然很简单，但却有很多应用场景，更是之后学习更高阶算法的起点。我们致力于用大量经典问题的例子来传递底层直觉。我们会展示变量的不同选择和能量的构建方式。在过去的二十余年，几何处理领域已经用最小二乘法来计算二维地图、形变、测地路径、标价场等问题。我们的例子提供了许多可以直接用最小二乘法求解的应用实例。注意线性回归是一个和许多其他科学领域有深刻联系的工具，我们提供了一些这样的参考来开阔读者的视野。

本课程面向了解如何用传统方式编程的学生/工程师/研究人员: 通过将复杂任务分解为操作组合结构(树、图、网格……)的基本操作。我们提出了一种不同的范式。在这种范式中，我们描述了一个好的结果是什么样的，并用数值优化算法来寻找结果。

![](https://raw.githubusercontent.com/ssloy/least-squares-course/master/manuscript/img/caricature.jpg)

