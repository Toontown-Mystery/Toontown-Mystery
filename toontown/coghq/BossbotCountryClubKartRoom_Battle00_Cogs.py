from SpecImports import *
import random
from toontown.toonbase import ToontownGlobals
CogParent = 110400
BattleCellId = 0
BattleCells = {BattleCellId: {'parentEntId': CogParent,
                'pos': Point3(0, 0, 0)}}
CogData = [{'type': 'dot',
  'parentEntId': CogParent,
  'boss': 0,
  'level': 22,
  'battleCell': BattleCellId,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'type': 'wrd',
  'parentEntId': CogParent,
  'boss': 0,
  'level': 21,
  'battleCell': BattleCellId,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'type': 'tbc',
  'parentEntId': CogParent,
  'boss': 0,
  'level': 20,
  'battleCell': BattleCellId,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'type': 'wrd',
  'parentEntId': CogParent,
  'boss': 0,
  'level': 21,
  'battleCell': BattleCellId,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0}]
ReserveCogData = []
