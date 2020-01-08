使用Python编程实现人员疏散模拟

包含三个模块 `main.py` `map.py` `people.py`

## main.py
界面实现，包含GUI类，显示地图、人员、疏散情况等信息

## map.py
地图类，地图以点(px, py)集形式保存出口Exit位置及障碍物Barrier位置
出口对地图的势能初始化：利用BFS算法实现，多个出口取最小势能

## people.py
包含两个类，Person类和People类，前者只有移动速度、位置等基本属性，后者包含了整个地图信息，人流密度等，方便指引每个人的移动
