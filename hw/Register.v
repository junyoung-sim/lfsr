`ifndef REGISTER
`define REGISTER

module Register#(
  parameter nbits=8
) (
  (* keep=1 *) input  logic             clk,
  (* keep=1 *) input  logic             rst,
  (* keep=1 *) input  logic             en,
  (* keep=1 *) input  logic [nbits-1:0] d,
  (* keep=1 *) output logic [nbits-1:0] q
);

  always @(posedge clk) begin
    if(rst)
      q <= {nbits{1'b0}};
    else if(en)
      q <= d;
    else
      q <= q;
  end

endmodule

`endif