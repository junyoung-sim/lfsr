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

  await RisingEdge(dut.clk)
  assert dut.active.value == active, "FAILED (active)"
  assert dut.out.value == out, "FAIELD (out)"

#=================================================================
# test_reset
#=================================================================

@cocotb.test()
async def test_reset(dut):
  clock = Clock(dut.clk, 10, units="ns")
  cocotb.start_soon(clock.start(start_high=False))

  #                rst start stop tap         seed        act out
  await check( dut, 1,   0,   0,  0b00011101, 0b11100011, x,  x )
  await check( dut, 0,   0,   0,  0b00011101, 0b11100011, 0,  1 )
  await check( dut, 0,   0,   0,  0b00011101, 0b11100011, 0,  1 )
  