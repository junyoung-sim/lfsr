import random
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import *

x = 'xxxxxxxx'

async def check(dut, rst, en, shift_in, seed, q):
  dut.rst.value      = rst
  dut.en.value       = en
  dut.shift_in.value = shift_in
  dut.seed.value     = seed
  
  await RisingEdge(dut.clk)
  assert dut.q.value == q, "FAILED"

#=========================================================
# test_reset
#=========================================================

@cocotb.test()
async def test_reset(dut):
  clock = Clock(dut.clk, 10, units="ns")
  cocotb.start_soon(clock.start(start_high=False))

  #                rst en in seed q
  await check( dut, 1, 0, 0, 0,   x   )
  await check( dut, 1, 0, 0, 255, 0   )
  await check( dut, 0, 0, 0, 0,   255 )
  await check( dut, 0, 0, 0, 0,   255 )

#=========================================================
# test_shift
#=========================================================

@cocotb.test()
async def test_shift(dut):
  clock = Clock(dut.clk, 10, units="ns")
  cocotb.start_soon(clock.start(start_high=False))

  #                rst en in seed q
  await check( dut, 1, 0, 0, 0,   x           )
  await check( dut, 0, 1, 1, 0,   0b0000_0000 )
  await check( dut, 0, 1, 0, 0,   0b1000_0000 )
  await check( dut, 0, 0, 1, 0,   0b0100_0000 )
  await check( dut, 0, 0, 0, 0,   0b0100_0000 )
  await check( dut, 0, 1, 0, 0,   0b0100_0000 )
  await check( dut, 0, 1, 0, 0,   0b0010_0000 )
  await check( dut, 0, 1, 0, 0,   0b0001_0000 )
  await check( dut, 0, 1, 1, 0,   0b0000_1000 )
  await check( dut, 0, 1, 0, 0,   0b1000_0100 )
  await check( dut, 0, 1, 1, 0,   0b0100_0010 )
  await check( dut, 0, 1, 0, 0,   0b1010_0001 )
  await check( dut, 0, 1, 0, 0,   0b0101_0000 )

#=========================================================
# test_random
#=========================================================

@cocotb.test()
async def test_random(dut):
  clock = Clock(dut.clk, 10, units="ns")
  cocotb.start_soon(clock.start(start_high=False))

  await check( dut, 1, 0, 0, 0, x )

  expected = 0
  for i in range(1000):
    rst      = random.randint(0, 1)
    en       = random.randint(0, 1)
    shift_in = random.randint(0, 1)
    seed     = random.randint(0, 255)

    await check( dut, rst, en, shift_in, seed, expected)

    if rst:
      expected = seed
    elif en:
      expected = (expected >> 1) | shift_in * pow(2,7)
    else:
      expected = expected
