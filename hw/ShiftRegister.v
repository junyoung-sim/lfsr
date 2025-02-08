`ifndef SHIFT_REGISTER
`define SHIFT_REGISTER

module ShiftRegister
#(
  parameter nbits=8
)(
  input  logic             clk,
  input  logic             rst,
  input  logic             en,
  input  logic             shift_in,
  input  logic [nbits-1:0] seed,
  output logic [nbits-1:0] q
);

  always_ff @(posedge clk) begin
    if(rst)
      q <= seed;
    else if(en) begin
      for(int i = 0; i < nbits-1; i++)
        q[i] <= q[i+1];
      q[nbits-1] <= shift_in;
    end
    else
      q <= q;
  end

endmodule

`endif