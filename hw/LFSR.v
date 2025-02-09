`ifndef LINEAR_FEEDBACK_SHIFT_REGISTER
`define LINEAR_FEEDBACK_SHIFT_REGISTER

`include "ShiftRegister.v"

module LFSR
#(
  parameter nbits=8
)(
  input  logic             clk,
  input  logic             rst,
  input  logic             en,
  input  logic [nbits-1:0] tap,
  input  logic [nbits-1:0] seed,
  output logic             out
);

  logic             shift_in;
  logic [nbits-1:0] shift_reg_q;

  ShiftRegister shift_reg
  (
    .clk      (clk),
    .rst      (rst),
    .en       (en),
    .shift_in (shift_in),
    .seed     (seed),
    .q        (shift_reg_q)
  );

  always_comb begin
    shift_in = shift_reg_q[0];
    for(int i = 1; i < nbits; i++) begin
      if(tap[i])
        shift_in = shift_in ^ shift_reg_q[i];
    end
  end

  assign out = shift_reg_q[0];

endmodule

`endif
