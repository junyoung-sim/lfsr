`ifndef RANDOM_ENGINE_CTRL
`define RANDOM_ENGINE_CTRL

`include "../hw/Register.v"

module RandomEngineCtrl (
  (* keep=1 *) input  logic clk,
  (* keep=1 *) input  logic rst,

  // I/O Interface

  (* keep=1 *) input  logic go,
  (* keep=1 *) output logic done_val,

  // Control Signals (RandomEngineCtrl -> RandomEngineDpath)

  (* keep=1 *) output logic itr_init,
  (* keep=1 *) output logic itr_en,
  (* keep=1 *) output logic lfsr_en,

  // Status Signals (RandomEngineDpath -> RandomEngineCtrl)

  (* keep=1 *) input  logic done
);

  // State Encodings

  localparam STATE_WAIT  = 2'b00;
  localparam STATE_SHIFT = 2'b01;
  localparam STATE_DONE  = 2'b10;

  // State Register

  logic [1:0] state;
  logic [1:0] state_next;

  Register#(2) rand_engine_state (
    .clk(clk),
    .rst(rst),
    .en(1'b1),
    .d(state_next),
    .q(state)
  );

  // State Transition Logic

  always @(*) begin
    case(state)
      STATE_WAIT : state_next = (go ? STATE_SHIFT : STATE_WAIT);
      STATE_SHIFT: state_next = (done ? STATE_DONE : STATE_SHIFT);
      STATE_DONE : state_next = STATE_DONE;
      default: state_next = STATE_WAIT;
    endcase
  end

  // Output Logic

  always @(*) begin
    case(state)
      STATE_WAIT: begin
        done_val = 0;
        itr_init = go;
        itr_en   = go;
        lfsr_en  = 0;
      end
      STATE_SHIFT: begin
        done_val = 0;
        itr_init = 0;
        itr_en   = 1;
        lfsr_en  = 1;
      end
      STATE_DONE: begin
        done_val = 1;
        itr_init = 0;
        itr_en   = 0;
        lfsr_en  = 0;
      end
      default: begin
        done_val = 0;
        itr_init = go;
        itr_en   = go;
        lfsr_en  = 0;
      end
    endcase
  end

endmodule

`endif