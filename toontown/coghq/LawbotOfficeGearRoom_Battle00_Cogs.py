from SpecImports import *
import random
from toontown.toonbase import ToontownGlobals
CogParent = 10000
CogParent1 = 10002
CogParent2 = 10004
CogParent3 = 10007
BattlePlace1 = 10000
BattlePlace2 = 10002
BattlePlace3 = 10004
BattlePlace4 = 10007
BattleCellId = 0
Battle2CellId = 1
Battle3CellId = 2
Battle4CellId = 3
BattleCells = {BattleCellId: {'parentEntId': BattlePlace1,
                'pos': Point3(0, 0, 0)},
 Battle2CellId: {'parentEntId': BattlePlace2,
                'pos': Point3(0, 0, 0)},
 Battle3CellId: {'parentEntId': BattlePlace3,
                'pos': Point3(0, 0, 0)},
 Battle4CellId: {'parentEntId': BattlePlace4,
                     'pos': Point3(0, 0, 0)}}
CogData = [{'parentEntId': CogParent,
  'boss': 0,
  'level': 16,
  'battleCell': BattleCellId,
  'pos': Point3(-8, 4, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': 17,
  'battleCell': BattleCellId,
  'pos': Point3(-3, 4, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': 15,
  'battleCell': BattleCellId,
  'pos': Point3(3, 4, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': 16,
  'battleCell': BattleCellId,
  'pos': Point3(8, 4, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
{'parentEntId': CogParent1,
  'boss': 0,
  'level': 10,
  'battleCell': Battle2CellId,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'parentEntId': CogParent1,
  'boss': 0,
  'level': 11,
  'battleCell': Battle2CellId,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'parentEntId': CogParent1,
  'boss': 0,
  'level': 10,
  'battleCell': Battle2CellId,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'parentEntId': CogParent1,
  'boss': 0,
  'level': 11,
  'battleCell': Battle2CellId,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
{'parentEntId': CogParent2,
  'boss': 0,
  'level': 11,
  'battleCell': Battle3CellId,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'parentEntId': CogParent2,
  'boss': 0,
  'level': 12,
  'battleCell': Battle3CellId,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'parentEntId': CogParent2,
  'boss': 0,
  'level': 10,
  'battleCell': Battle3CellId,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'parentEntId': CogParent2,
  'boss': 0,
  'level': 10,
  'battleCell': Battle3CellId,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
{'parentEntId': CogParent3,
  'boss': 0,
  'level': 11,
  'battleCell': Battle4CellId,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'parentEntId': CogParent3,
  'boss': 0,
  'level': 11,
  'battleCell': Battle4CellId,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'parentEntId': CogParent3,
  'boss': 0,
  'level': 11,
  'battleCell': Battle4CellId,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'parentEntId': CogParent3,
  'boss': 0,
  'level': 11,
  'battleCell': Battle4CellId,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1}]
ReserveCogData = []
