`ifndef RANDOM_ENGINE_CTRL
`define RANDOM_ENGINE_CTRL

`include "../hw/Register.v"

module RandomEngineCtrl (
  (* keep=1 *) input  logic clk,
  (* keep=1 *) input  logic rst,

  // I/O Interface

  (* keep=1 *) input  logic start,
  (* keep=1 *) input  logic stop,
  (* keep=1 *) output logic active,

  // Control Signal (RandomEngineCtrl -> RandomEngineDpath)
  
  (* keep=1 *) output logic lfsr_en
);

  // State Encodings

  localparam STATE_WAIT = 1'b0;
  localparam STATE_LFSR = 1'b1;

  // State Register

  logic state;
  logic state_next;

  Register#(1) state_reg (
    .clk(clk),
    .rst(rst),
    .en(1'b1),
    .d(state),
    .q(state_next)
  );

  // State Transition Logic

  always @(*) begin
    case(state)
      STATE_WAIT: state_next = (start ? STATE_LFSR : STATE_WAIT);
      STATE_LSFR: state_next = (stop  ? STATE_WAIT : STATE_LFSR);
    endcase
  end

  // Output Logic

  always @(*) begin
    case(state)
      STATE_WAIT: begin
        active  = 0;
        lfsr_en = 0;
      end
      STATE_LFSR: begin
        active  = 1;
        lfsr_en = 1;
      end
    endcase
  end

endmodule

`endif