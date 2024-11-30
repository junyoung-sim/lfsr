`ifndef RANDOM_ENGINE
`define RANDOM_ENGINE

`include "../hw/RandomEngineCtrl.v"
`include "../hw/RandomEngineDpath.v"

module RandomEngine (
  (* keep=1 *) input  logic       clk,
  (* keep=1 *) input  logic       rst,
  (* keep=1 *) input  logic       start,
  (* keep=1 *) input  logic       stop,
  (* keep=1 *) input  logic [7:0] tap,
  (* keep=1 *) input  logic [7:0] seed,
  (* keep=1 *) output logic       active,
  (* keep=1 *) output logic       out
);

  logic lfsr_en;

  RandomEngineCtrl ctrl
  (
    .*
  );

  RandomEngineDpath dpath
  (
    .*
  );

endmodule

`endif