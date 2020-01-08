# Louvre_Evacuation
来源：2019年 美赛 D题

## 问题背景
  法国发生的恐怖袭击越来越多，在许多热门目的地，亟需一个应对紧急情况的疏散计划。
你们的ICM团队正在帮助设计在法国巴黎**卢浮宫的疏散计划**。
总的来说，疏散的目标是让所有的人都撤离，尽快安全离开大楼。
接到疏散通知后，为了尽快清空建筑，每个人尽可能的通过一个最佳出口。

## 问题要求
  建立一个卢浮宫紧急疏散模型，以满足：
  - 当出现突发意外事件时，指导游客人群从卢浮宫疏散 (evacuate visitors from the museum)
  - 探讨安保/急救人员进入策略 (allow emergency personnel to enter the building)
  - 确定人流移动的瓶颈 (identify potential bottlenecks limiting movement towards the exits)
  - 模型考虑各种威胁 (a broad set of considerations and various types of potential threats)

--------
# My Work:
不考虑个体行为的情况下，可以将卢浮宫抽象为二维平面图，记录各个关键节点、出口、节点之间的长度、路径信息等，建立图论模型，求解最短路、网络流等，从而得到疏散时间，瓶颈等结果。

从人群疏散的角度看，查阅资料，我们发现目前疏散模型大致有两种处理方式，**元胞自动机**模型和**社会力**模型。
本程序主要模拟了人员疏散的撤离情况。

## 编程目的
  - 研究人群在一般空间的流动情况
  - 出口数量、分布对疏散时间的影响
  - 障碍物对人员流动的影响
  - 定量求解人流密度，确定疏散瓶颈
  
## 算法思想
利用元胞自动机实现 （社会力模型人员会在地图上重叠）
  - 初始化地图，地图为矩形区域，基本信息包含长Length、宽Width、若干出口Exit、障碍物Barrier等
  - 基于该[论文](https://github.com/izcat/Louvre_Evacuation/blob/master/ref/元胞自动机疏散模拟的并行计算研究与实现_金自豪.caj)，出口距离在地图上反映为势能的高低，初始化地图的**势能**
  - 初始化人群，人群随机分布在地图的合法区域内
  - 疏散模拟：
    - 移动方向：每个人优先选择最短路进行撤离，考虑使用Moore型元胞，有8个移动方向
    - 移动速度：一定区域内（周围8个邻居元胞）人流密度决定人员的移动速度 （待改进：统计可视角度内的人流密度）

## 模拟结果
### 人员疏散过程模拟
![gif1](https://github.com/izcat/Louvre_Evacuation/blob/master/result/1.gif)
![gif2](https://github.com/izcat/Louvre_Evacuation/blob/master/result/2.gif)
![png3](https://github.com/izcat/Louvre_Evacuation/blob/master/result/3.png)
![png4](https://github.com/izcat/Louvre_Evacuation/blob/master/result/4.png)


### 热力图
反映瓶颈位置  

![pic1](https://github.com/izcat/Louvre_Evacuation/blob/master/result/figure_1.png)
![pic2](https://github.com/izcat/Louvre_Evacuation/blob/master/result/figure_2.png)
    
