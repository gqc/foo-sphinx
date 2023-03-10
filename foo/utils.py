def do_nothing():
  "this function does nothing"
  return

from constants import CONSTANT_1
from enums import Constant as C

assert C.CONSTANT_1.value == CONSTANT_1, "values are not equal"