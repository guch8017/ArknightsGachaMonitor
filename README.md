# ArknightsGachaMonitor
基于明日方舟客户端本身的抽卡模拟器。
### 当前对应客户端版本：0.7.28
## 使用
### 环境
* Python 2.7(.15)
* Flask
Flask安装：
```bash
pip install flask
```
### 开始运行
```bash
git clone https://github.com/guch8017/ArknightsGachaMonitor.git
cd ArknightsGachaMonitor/src
python app.py
```
### 数据导向更改
通过Charles将游戏封包数据导向抽卡模拟器实现模拟抽卡效果
安装Charles SSL证书并确定能成功解码手机/模拟器的https数据后，进行下列操作：
* 选中 Tools - Map Remote （macOS快捷键 option+command+M）
* 点击Add，添加一条转发规则，如下图填写参数
![map.png](https://github.com/guch8017/ArknightsGachaMonitor/raw/master/images/map.png)
抽卡前需确保合成玉数量>=6000。否则请进行以下操作修改本地的合成玉数量。
* 再次点击Add，添加以下规则。
![syncData.png](https://github.com/guch8017/ArknightsGachaMonitor/raw/master/images/syncData.png)
最后确保将Enable Map Remote开关选中，重新登陆游戏即可。

## 样例
以下是模拟全六星的截图
![example1](https://github.com/guch8017/ArknightsGachaMonitor/raw/master/images/example1.png)
![example2](https://github.com/guch8017/ArknightsGachaMonitor/raw/master/images/example2.png)

## 更新日志
### 0.0.1
~~部分角色皮肤出现问题，已知原因为部分角色皮肤非常规命名（干员名#1），待修复。~~ 
修正偶尔出现空白人物的bug。确认到为部分召唤物与人物数据共同存储导致问题，已修复。

## Bugs&Todos
1. 计划添加指定抽取人物功能，你也可以去豹跳了（误）。
2. 信物获取数据暂未添加，故不会出现信物/黄票获取界面。
3. 添加抽取统计，是欧是非一看便知。
4. 貌似可以抽出暴行，阿米娅。。。

## 感谢
角色数据来源：[ArknightsGameData](https://github.com/Perfare/ArknightsGameData)

