`ifndef RANDOM_ENGINE_DPATH
`define RANDOM_ENGINE_DPATH

`include "LFSR.v"

module RandomEngineDpath
(
  input  logic       clk,
  input  logic       rst,

  // I/O Interface

  input  logic [7:0] tap,
  input  logic [7:0] seed,
  output logic       out,

  // Control Signals

  input  logic       lfsr_en
);

  logic lfsr_out;

  LFSR lfsr
  (
    .clk  (clk),
    .rst  (rst),
    .en   (lfsr_en),
    .tap  (tap),
    .seed (seed),
    .out  (lfsr_out)
  );

  assign out = lfsr_out;

endmodule

`endif