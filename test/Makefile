TOPLEVEL_LANG ?= verilog
SIM := vcs

PWD=$(shell pwd)
export PYTHONPATH := $(PWD):$(PYTHONPATH)

VERILOG_SOURCES=$(HOME)/c2s2/lfsr/hw/RandomEngine.v

COMPILE_ARGS += +incdir+$(HOME)/c2s2/lfsr/hw/

TOPLEVEL=RandomEngine
MODULE=RandomEngine_test

WAVES=1
COVER=1

ifeq ($(WAVES), 1)
	EXTRA_ARGS += +vcs+dumpvars+waves.vcd
endif

ifeq ($(COVER), 1)
	COMPILE_ARGS += -cm line+tgl
	SIM_ARGS += -cm line+tgl
endif

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all:
	rm -f waves.vcd
	rm -rf coverage_report
	rm -f results.xml
	make clean

coverage_report:
	urg -dir ./sim_build/simv.vdb -format both -report ./coverage_report
