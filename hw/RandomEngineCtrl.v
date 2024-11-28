`ifndef RANDOM_ENGINE_CTRL
`define RANDOM_ENGINE_CTRL

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

endmodule;

`endif