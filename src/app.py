# -*- coding: utf-8 -*-
from flask import Flask
import json
import random
from copy import deepcopy
from time import time

app = Flask(__name__)

# 常量部分
startAdd = 50  # 保底数量(修改为0时无保底)
percentageSSSR = 100  # 六星概率
percentageSSSRAdd = 2  # 保底概率增加
percentageSSR = 8  # 五星概率
percentageSR = 50  # 四星概率
chanceUp = [[], [], [], []]  # 特殊UP活动,分别对应3、4、5、6

# 传输格式常量
dataResponse = {"gachaResultList": [], "playerDataDelta": {}}
gachaResultList = {"charInstId": -1, "charId": "", "isNew": 1, "itemGet": []}
itemGet = {"type": "", "id": "", "count": -1}
status = {"diamondShard": 10000, "hggShard": 0, "lggShard": 0}
playerDataDelta = {"modified": {}, "deleted": {}}
modified = {"status": {}, "troop": {}, "inventory": {}}  # , "dexNav": {}, "building": {}
troop = {"chars": {}, "curCharInstId": -1}
troopChar = {"instId": -1, "charId": "", "favorPoint": 0, "potentialRank": 0, "mainSkillLvl": 1,
             "skin": "char_290_vigna#1", "level": 1, "exp": 0, "evolvePhase": 0, "defaultSkillIndex": 0,
             "gainTime": -1, "skills": []}

# 统计用变量
listR = [[], [], [], []]  # 干员列表
listCount = [[], [], [], []]  # 抽取数量统计
total = 0  # 总抽取数量
save = 0  # 保底统计


def db_init():
    global listR, listCount
    print('HelloWorld')
    with open('''/''', 'r') as infile:
        js = json.loads(infile.read())

        for (key, value) in js.items():
            rarity = value["rarity"]
            if rarity > 1:
                listR[rarity - 2].append(key)
                listCount[rarity - 2].append(0)


def getChance():
    sssr_percentage = percentageSSSR
    if startAdd == 0:
        return sssr_percentage
    if save > startAdd:
        sssr_percentage += (save - startAdd) * percentageSSSRAdd
    return sssr_percentage


def getGachaItem(rarity):
    l1 = len(listR[rarity - 3])
    l2 = len(chanceUp[rarity - 3])
    if l2 != 0:
        if random.randrange(1, 3) == 1:
            return chanceUp[rarity - 3][random.randrange(0, l2)]
    return listR[rarity - 3][random.randrange(0, l1)]


def gachaGetList():
    global total, save
    gachaList = []
    for i in range(10):
        s = random.randrange(1, 101)
        chance = getChance()
        print 'S:{}, Chance:{}'.format(s, chance)
        if s <= chance:
            print('SSSR')
            total += 1
            save = 0
            gachaList.append(getGachaItem(6))
        elif s <= chance + percentageSSR:
            print('SSR')
            total += 1
            save += 1
            gachaList.append(getGachaItem(5))
        elif s <= chance + percentageSSR + percentageSR:
            print('SR')
            total += 1
            save += 1
            gachaList.append(getGachaItem(4))
        else:
            print('R')
            total += 1
            save += 1
            gachaList.append(getGachaItem(3))
    return gachaList


def dataTest():
    if startAdd < 0:
        return False
    if percentageSSSR < 0 or percentageSSSR > 100:
        return False
    if percentageSSSRAdd < 0:
        return False
    return True


def generateData(charList):
    gacha_list = []
    troop_chars_dict = {}
    t = time()
    i = 15
    for char_info in charList:
        troop_data = deepcopy(troopChar)
        troop_data.update({'instId': '{}'.format(i), 'charId': char_info, 'skin': '{}#1'.format(char_info),
                           'gainTime': '{}'.format(int(t))})
        troop_chars_dict.update({'{}'.format(i): troop_data})
        gacha_data = deepcopy(gachaResultList)
        gacha_data.update({'charInstId': i, 'charId': char_info})
        gacha_list.append(gacha_data)
        i += 1
    player_data = deepcopy(playerDataDelta)
    modified_data = deepcopy(modified)
    troop_data_main = deepcopy(troop)
    troop_data_main.update({'curCharInstId': i, 'chars': troop_chars_dict})
    modified_data.update({'status': status, 'troop': troop_data_main})
    data_response = deepcopy(dataResponse)
    player_data.update({'modified': modified_data})
    data_response.update({'gachaResultList': gacha_list, 'playerDataDelta': player_data})
    return data_response


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/gacha/syncNormalGacha')
def syncGacha():
    return json.dumps({
        "playerDataDelta": {
            "modified": {},
            "deleted": {}
        }
    })


@app.route('/account/syncData', methods=['POST', 'GET'])
def syncData():
    with open('''syncData.json''', 'r') as sync_data_json:
        return sync_data_json.read()


@app.route('/showDb')
def print_db():
    return json.dumps(listR)


@app.route('/gacha/tenAdvanceGacha', methods=['POST', 'GET'])
def gacha():
    return json.dumps(generateData(gachaGetList()))


db_init()
if __name__ == '__main__':
    if dataTest():
        app.run()
