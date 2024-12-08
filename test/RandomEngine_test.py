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

def lfsr(shift_reg_q, tap):
  shift_in = shift_reg_q & 1
  for i in range(1, 8):
    if (tap >> i) & 1:
      tapped = (shift_reg_q >> i) & 1
      shift_in = shift_in ^ tapped
      
  shift_reg_q = shift_reg_q >> 1
  shift_reg_q = shift_reg_q | shift_in * pow(2,7)
  
  out = shift_reg_q & 1

  return shift_reg_q, out

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

#=================================================================
# test_simple
#=================================================================

@cocotb.test()
async def test_simple(dut):
  clock = Clock(dut.clk, 10, units="ns")
  cocotb.start_soon(clock.start(start_high=False))

  # check manually computed active/output signals

  #                rst start stop tap         seed        act out
  await check( dut, 1,   0,   0,  0b00011101, 0b11100011, x,  x )
  await check( dut, 0,   0,   0,  0b00011101, 0b11100011, 0,  1 )
  await check( dut, 0,   1,   0,  0b00011101, 0b11100011, 0,  1 )
  await check( dut, 0,   0,   0,  0b00011101, 0b11100011, 1,  1 )
  await check( dut, 0,   0,   0,  0b00011101, 0b11100011, 1,  0 )
  await check( dut, 0,   0,   0,  0b00011101, 0b11100011, 1,  0 )
  await check( dut, 0,   0,   0,  0b00011101, 0b11100011, 1,  0 )
  await check( dut, 0,   0,   0,  0b00011101, 0b11100011, 1,  1 )
  await check( dut, 0,   0,   0,  0b00011101, 0b11100011, 1,  1 )
  await check( dut, 0,   0,   0,  0b00011101, 0b11100011, 1,  1 )
  await check( dut, 0,   0,   0,  0b00011101, 0b11100011, 1,  1 )
  await check( dut, 0,   0,   0,  0b00011101, 0b11100011, 1,  0 )
  await check( dut, 0,   0,   0,  0b00011101, 0b11100011, 1,  0 )
  await check( dut, 0,   0,   0,  0b00011101, 0b11100011, 1,  1 )
  await check( dut, 0,   0,   0,  0b00011101, 0b11100011, 1,  1 )
  await check( dut, 0,   0,   0,  0b00011101, 0b11100011, 1,  1 )
  await check( dut, 0,   0,   0,  0b00011101, 0b11100011, 1,  0 )
  await check( dut, 0,   0,   1,  0b00011101, 0b11100011, 1,  0 )
  await check( dut, 0,   0,   0,  0b00011101, 0b11100011, 0,  0 )

#=================================================================
# test_directed_tap_seed_1
#=================================================================

@cocotb.test()
async def test_directed_tap_seed_1(dut):
  clock = Clock(dut.clk, 10, units="ns")
  cocotb.start_soon(clock.start(start_high=False))

  # test LFSR 100,000 times with tap and seed from test_simple

  tap  = 0b00011101
  seed = 0b11100011

  await check( dut, 1, 0, 0, tap, seed, x, x )

  shift_reg_q = seed

  state = 0
  act   = 0
  out   = seed & 1

  for t in range(100000):
    start = random.randint(0, 1)
    stop  = random.randint(0, 1)

    await check( dut, 0, start, stop, tap, seed, act, out )

    if (state == 0) & (start == 0):
      state = 0
      act   = 0
      out   = out

    elif (state == 0) & (start == 1):
      state = 1
      act   = 1
      shift_reg_q, out = lfsr(shift_reg_q, tap)
    
    elif (state == 1) & (stop == 0):
      state = 1
      act   = 1
      shift_reg_q, out = lfsr(shift_reg_q, tap)
    
    elif (state == 1) & (stop == 1):
      state = 0
      act   = 0
      out   = out

#=================================================================
# test_directed_tap_seed_2
#=================================================================

@cocotb.test()
async def test_directed_tap_seed_2(dut):
  clock = Clock(dut.clk, 10, units="ns")
  cocotb.start_soon(clock.start(start_high=False))

  # test LFSR 100,000 times with the input tap's lsb set to zero
  # the lsb should still be included in the feedback function

  tap  = 0b00011100
  seed = 0b11100011

  await check( dut, 1, 0, 0, tap, seed, x, x )

  shift_reg_q = seed

  state = 0
  act   = 0
  out   = seed & 1

  for t in range(100000):
    start = random.randint(0, 1)
    stop  = random.randint(0, 1)

    await check( dut, 0, start, stop, tap, seed, act, out )

    if (state == 0) & (start == 0):
      state = 0
      act   = 0
      out   = out

    elif (state == 0) & (start == 1):
      state = 1
      act   = 1
      shift_reg_q, out = lfsr(shift_reg_q, tap)
    
    elif (state == 1) & (stop == 0):
      state = 1
      act   = 1
      shift_reg_q, out = lfsr(shift_reg_q, tap)
    
    elif (state == 1) & (stop == 1):
      state = 0
      act   = 0
      out   = out

#=================================================================
# test_directed_lockup
#=================================================================

@cocotb.test()
async def test_directed_lockup(dut):
  clock = Clock(dut.clk, 10, units="ns")
  cocotb.start_soon(clock.start(start_high=False))

  # test illegal state where the seed is zero
  # output signal should always be zero regardless of tap

  seed = 0b00000000

  await check( dut, 1, 0, 0, 0, seed, x, x )

  shift_reg_q = seed

  state = 0
  act   = 0
  out   = seed & 1

  for t in range(100000):
    tap   = random.randint(0, 255)
    start = random.randint(0, 1)
    stop  = random.randint(0, 1)

    await check( dut, 0, start, stop, tap, seed, act, out )

    if (state == 0) & (start == 0):
      state = 0
      act   = 0
      out   = out

    elif (state == 0) & (start == 1):
      state = 1
      act   = 1
      shift_reg_q, out = lfsr(shift_reg_q, tap)
    
    elif (state == 1) & (stop == 0):
      state = 1
      act   = 1
      shift_reg_q, out = lfsr(shift_reg_q, tap)
    
    elif (state == 1) & (stop == 1):
      state = 0
      act   = 0
      out   = out

#=================================================================
# test_random
#=================================================================

@cocotb.test()
async def test_random(dut):
  clock = Clock(dut.clk, 10, units="ns")
  cocotb.start_soon(clock.start(start_high=False))

  # test LFSR 1M times with all interfaces set randomly

  seed = random.randint(0, 255)

  await check( dut, 1, 0, 0, 0, seed, x, x )

  shift_reg_q = seed

  state = 0
  act   = 0
  out   = seed & 1

  for t in range(1000000):
    rst   = random.randint(0, 1)
    start = random.randint(0, 1)
    stop  = random.randint(0, 1)
    tap   = random.randint(0, 255)
    seed  = random.randint(0, 255)

    await check( dut, rst, start, stop, tap, seed, act, out )

    if rst:
      state  = 0
      act    = 0
      out    = seed & 1
      shift_reg_q = seed

    elif (state == 0) & (start == 0):
      state = 0
      act   = 0
      out   = out

    elif (state == 0) & (start == 1):
      state = 1
      act   = 1
      shift_reg_q, out = lfsr(shift_reg_q, tap)
    
    elif (state == 1) & (stop == 0):
      state = 1
      act   = 1
      shift_reg_q, out = lfsr(shift_reg_q, tap)
    
    elif (state == 1) & (stop == 1):
      state = 0
      act   = 0
      out   = out
