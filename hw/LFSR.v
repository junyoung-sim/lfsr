`ifndef LINEAR_FEEDBACK_SHIFT_REGISTER
`define LINEAR_FEEDBACK_SHIFT_REGISTER

`include "../hw/ShiftRegister.v"

module LFSR#(
  parameter nbits=8
) (
  (* keep=1 *) input  logic             clk,
  (* keep=1 *) input  logic             reset,
  (* keep=1 *) input  logic             enable,
  (* keep=1 *) input  logic [nbits-1:0] tap,
  (* keep=1 *) input  logic [nbits-1:0] seed,
  (* keep=1 *) output logic             out
);


endmodule

`endif
