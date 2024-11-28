`ifndef ADDER
`define ADDER

module Adder#(
  parameter nbits=8
) (
  (* keep=1 *) input  logic [nbits-1:0] in0,
  (* keep=1 *) input  logic [nbits-1:0] in1,
  (* keep=1 *) output logic [nbits-1:0] sum
);

  always @(*) begin
    sum = in0 + in1;
  end

endmodule

`endif