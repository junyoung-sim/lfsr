`ifndef COMPARATOR
`define COMPARATOR

module Comparator#(
  parameter nbits=8
) (
  (* keep=1 *) input  logic [nbits-1:0] in0,
  (* keep=1 *) input  logic [nbits-1:0] in1,
  (* keep=1 *) output logic             eq
);

  always @(*) begin
    eq = in0 == in1;
  end

endmodule

`endif