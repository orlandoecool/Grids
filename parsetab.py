
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'NAME CREATE DESTROY\n    grids : create\n    | destroy\n    | empty\n    \n    object : NAME\n    \n    create : CREATE object NAME\n    \n    destroy : DESTROY object NAME\n    \n    empty :\n    '
    
_lr_action_items = {'CREATE':([0,],[5,]),'DESTROY':([0,],[6,]),'$end':([0,1,2,3,4,10,11,],[-7,0,-1,-2,-3,-5,-6,]),'NAME':([5,6,7,8,9,],[8,8,10,-4,11,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'grids':([0,],[1,]),'create':([0,],[2,]),'destroy':([0,],[3,]),'empty':([0,],[4,]),'object':([5,6,],[7,9,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> grids","S'",1,None,None,None),
  ('grids -> create','grids',1,'p_grids','grids.py',33),
  ('grids -> destroy','grids',1,'p_grids','grids.py',34),
  ('grids -> empty','grids',1,'p_grids','grids.py',35),
  ('object -> NAME','object',1,'p_object','grids.py',41),
  ('create -> CREATE object NAME','create',3,'p_create','grids.py',47),
  ('destroy -> DESTROY object NAME','destroy',3,'p_destroy','grids.py',53),
  ('empty -> <empty>','empty',0,'p_empty','grids.py',62),
]
