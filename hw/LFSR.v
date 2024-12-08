`ifndef LINEAR_FEEDBACK_SHIFT_REGISTER
`define LINEAR_FEEDBACK_SHIFT_REGISTER

`include "../hw/ShiftRegister.v"

module LFSR#(
  parameter nbits=8
) (
  (* keep=1 *) input  logic             clk,
  (* keep=1 *) input  logic             rst,
  (* keep=1 *) input  logic             en,
  (* keep=1 *) input  logic [nbits-1:0] tap,
  (* keep=1 *) input  logic [nbits-1:0] seed,
  (* keep=1 *) output logic             out
);

  logic             shift_in;
  logic [nbits-1:0] shift_reg_q;

  ShiftRegister shift_reg (
    .clk(clk),
    .rst(rst),
    .en(en),
    .shift_in(shift_in),
    .seed(seed),
    .q(shift_reg_q)
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
