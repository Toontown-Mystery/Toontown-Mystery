from SpecImports import *
import random
from toontown.toonbase import ToontownGlobals
CogParent = 10000
LowerBattleParent = 10001
FrontCogParent = 10002
BattleCellId = 0
LowerBattleCellId = 1
FrontBattleCellId = 2
BattleCells = {BattleCellId: {'parentEntId': CogParent,
                'pos': Point3(0, 0, 0)},
 LowerBattleCellId: {'parentEntId': LowerBattleParent,
                     'pos': Point3(0, 0, 0)},
 FrontBattleCellId: {'parentEntId': FrontCogParent,
                     'pos': Point3(0, 0, 0)}}
CogData = [{'type': 'dm',
  'parentEntId': CogParent,
  'boss': 1,
  'level': 35,
  'battleCell': BattleCellId,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'type': 'csh',
  'parentEntId': CogParent,
  'boss': 0,
  'level': 23,
  'battleCell': BattleCellId,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'type': 'bgr',
  'parentEntId': CogParent,
  'boss': 0,
  'level': 26,
  'battleCell': BattleCellId,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'type': 'mes',
  'parentEntId': CogParent,
  'boss': 0,
  'level': 31,
  'battleCell': BattleCellId,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
{'type': 'ad',
  'parentEntId': LowerBattleParent,
  'boss': 0,
  'level': 22,
  'battleCell': LowerBattleCellId,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': LowerBattleParent,
  'boss': 0,
  'level': 11,
  'battleCell': LowerBattleCellId,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': LowerBattleParent,
  'boss': 0,
  'level': 11,
  'battleCell': LowerBattleCellId,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': LowerBattleParent,
  'boss': 0,
  'level': 11,
  'battleCell': LowerBattleCellId,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
{'type': 'rb',
  'parentEntId': FrontCogParent,
  'boss': 0,
  'level': 20,
  'battleCell': FrontBattleCellId,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'parentEntId': FrontCogParent,
  'boss': 0,
  'level': 11,
  'battleCell': FrontBattleCellId,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'parentEntId': FrontCogParent,
  'boss': 0,
  'level': 11,
  'battleCell': FrontBattleCellId,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'parentEntId': FrontCogParent,
  'boss': 0,
  'level': 11,
  'battleCell': FrontBattleCellId,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1}]
ReserveCogData = []
