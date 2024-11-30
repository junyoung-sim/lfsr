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

  logic lfsr_out;

  LFSR lfsr (
    .clk(clk),
    .rst(rst),
    .en(lfsr_en),
    .tap(tap),
    .seed(seed),
    .out(lfsr_out)
  );

  assign out = lfsr_out;

endmodule

`endif