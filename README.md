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
![map.png](https://github.com/guch8017/ArknightsGachaMonitor/images/map.png)
抽卡前需确保合成玉数量>=6000。否则请进行以下操作修改本地的合成玉数量。
* 再次点击Add，添加以下规则。
![syncData.png](https://github.com/guch8017/ArknightsGachaMonitor/images/syncData.png)
最后确保将Enable Map Remote开关选中，重新登陆游戏即可。

## Bugs&Todos
1. 部分角色皮肤出现问题，已知原因为部分角色皮肤非常规命名（干员名#1），待修复。
2. 计划添加指定抽取人物功能，你也可以去豹跳了（误）。
3. 信物获取数据暂未添加，故不会出现信物/黄票获取界面。
4. 添加抽取统计，是欧是非一看便知。
5. 貌似可以抽出暴行，阿米娅。。。

## 感谢
角色数据来源：[ArknightsGameData](https://github.com/Perfare/ArknightsGameData)

