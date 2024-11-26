module cocotb_iverilog_dump();
initial begin
    $dumpfile("sim_build/LFSR.fst");
    $dumpvars(0, LFSR);
end
endmodule
