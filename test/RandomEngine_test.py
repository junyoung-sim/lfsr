import random
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import *

x = 'x'

async def check(dut, rst, start, stop, tap, seed, active, out):
  dut.rst.value   = rst
  dut.start.value = start
  dut.stop.value  = stop
  dut.tap.value   = tap
  dut.seed.value  = seed

  assert dut.active.value == active, "FAILED (active)"
  assert dut.out.value == out, "FAIELD (out)"

#=========================================================
# test_simple
#=========================================================