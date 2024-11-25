module cocotb_iverilog_dump();
initial begin
    $dumpfile("sim_build/ShiftRegister.fst");
    $dumpvars(0, ShiftRegister);
end
endmodule
