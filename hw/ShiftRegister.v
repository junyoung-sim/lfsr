`ifndef SHIFT_REGISTER
`define SHIFT_REGISTER

module ShiftRegister#(
  parameter nbits=8
)(
  (* keep=1 *) input  logic              clk,
  (* keep=1 *) input  logic            reset,
  (* keep=1 *) input  logic           enable,
  (* keep=1 *) input  logic         shift_in,
  (* keep=1 *) input  logic [nbits-1:0] seed,
  (* keep=1 *) output logic [nbits-1:0] q
);

  always @(posedge clk) begin
    if(reset)
      q <= seed;
    else if(enable) begin
      for(int i = 0; i < nbits-1; i++)
        q[i] <= q[i+1];
      q[nbits-1] <= shift_in;
    end
    else
      q <= q;
  end

endmodule

`endif