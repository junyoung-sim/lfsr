`ifndef RANDOM_ENGINE_DPATH
`define RANDOM_ENGINE_DPATH

`include "../hw/LFSR.v"

module RandomEngineDpath (
  (* keep=1 *) input  logic       clk,
  (* keep=1 *) input  logic       rst,

  // I/O Interface

  (* keep=1 *) input  logic [7:0] tap,
  (* keep=1 *) input  logic [7:0] seed,
  (* keep=1 *) output logic       out,

  // Control Signals (RandomEngineCtrl -> RandomEngineDpath)

  (* keep=1 *) input  logic       lfsr_en
);



endmodule

`endif