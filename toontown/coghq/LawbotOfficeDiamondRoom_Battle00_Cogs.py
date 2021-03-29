from SpecImports import *
import random
from toontown.toonbase import ToontownGlobals
CogParent = 10000
BattlePlace1 = 10000
BattleCellId = 0
BattleCells = {BattleCellId: {'parentEntId': BattlePlace1,
                'pos': Point3(0, 0, 0)}}
CogData = [{'parentEntId': CogParent,
  'boss': 0,
  'level': 20,
  'battleCell': BattleCellId,
  'pos': Point3(-8, 4, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': 20,
  'battleCell': BattleCellId,
  'pos': Point3(-3, 4, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': 20,
  'battleCell': BattleCellId,
  'pos': Point3(3, 4, 0),
  'h': 180,
  'behavior': 'stand',
  'revives': random.choice([0, 1, 2]),
  'path': None,
  'skeleton': 0},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': 20,
  'battleCell': BattleCellId,
  'pos': Point3(8, 4, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0}]
ReserveCogData = []
