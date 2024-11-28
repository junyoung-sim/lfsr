import random
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import *

x = 'x'

async def check(dut, rst, en, tap, seed, expected):
  dut.rst.value  = rst
  dut.en.value   = en
  dut.tap.value  = tap
  dut.seed.value = seed

  await RisingEdge(dut.clk)
  assert dut.out.value == expected, "FAILED"

#=========================================================
# test_simple
#=========================================================

@cocotb.test()
async def test_simple(dut):
  clock = Clock(dut.clk, 10, units="ns")
  cocotb.start_soon(clock.start(start_high=False))

  tap  = 0b00011101
  seed = 0b11100011

  await check( dut, 1, 0, tap, seed, x )
  await check( dut, 0, 1, tap, seed, 1 ) # seed
  await check( dut, 0, 1, tap, seed, 1 ) #
  await check( dut, 0, 1, tap, seed, 0 ) #
  await check( dut, 0, 1, tap, seed, 0 ) #
  await check( dut, 0, 1, tap, seed, 0 ) #
  await check( dut, 0, 1, tap, seed, 1 ) #
  await check( dut, 0, 1, tap, seed, 1 ) #
  await check( dut, 0, 1, tap, seed, 1 ) #
  await check( dut, 0, 1, tap, seed, 1 ) # feedback
  await check( dut, 0, 1, tap, seed, 0 ) #
  await check( dut, 0, 1, tap, seed, 0 ) #
  await check( dut, 0, 1, tap, seed, 1 ) #
  await check( dut, 0, 1, tap, seed, 1 ) #
  await check( dut, 0, 1, tap, seed, 1 ) #
  await check( dut, 0, 1, tap, seed, 0 ) #
  await check( dut, 0, 1, tap, seed, 0 ) #

#=========================================================
# test_extensive
#=========================================================

@cocotb.test()
async def test_extensive(dut):
  clock = Clock(dut.clk, 10, units="ns")
  cocotb.start_soon(clock.start(start_high=False))

  tap  = 0b00011101
  seed = 0b11100011

  await check( dut, 1, 0, tap, seed, x )
  
  shift_reg_q = seed
  expected    = seed & 1

  for t in range(1000):
    await check( dut, 0, 1, tap, seed, expected )

    shift_in = shift_reg_q & 1
    for i in range(1, 8):
      if (tap >> i) & 1:
        tapped = (shift_reg_q >> i) & 1
        shift_in = shift_in ^ tapped
    
    shift_reg_q = shift_reg_q >> 1
    shift_reg_q = shift_reg_q | shift_in * pow(2,7)
    expected    = shift_reg_q & 1

#=========================================================
# test_random
#=========================================================

@cocotb.test()
async def test_random(dut):
  clock = Clock(dut.clk, 10, units="ns")
  cocotb.start_soon(clock.start(start_high=False))

  tap  = random.randint(0, 255)
  seed = random.randint(0, 255)

  await check( dut, 1, 0, tap, seed, x )
  
  shift_reg_q = seed
  expected    = seed & 1

  for t in range(1000):
    tap = random.randint(0, 255)
    
    await check( dut, 0, 1, tap, seed, expected )

    shift_in = shift_reg_q & 1
    for i in range(1, 8):
      if (tap >> i) & 1:
        tapped = (shift_reg_q >> i) & 1
        shift_in = shift_in ^ tapped
    
    shift_reg_q = shift_reg_q >> 1
    shift_reg_q = shift_reg_q | shift_in * pow(2,7)
    expected    = shift_reg_q & 1