`ifndef TT10_LFSR
`define TT10_LFSR

`include "LFSR.v"

module TT10_LFSR
(
  input  logic             clk,
  input  logic             rst,
  input  logic             en,
  input  logic [nbits-1:0] tap,
  output logic             out
);

  LFSR #(8) lfsr
  (
    .clk  (clk),
    .rst  (rst),
    .en   (en),
    .tap  (tap),
    .seed (8'b0),
    .out  (out)
  );

endmodule

`endif