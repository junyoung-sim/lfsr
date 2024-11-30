module cocotb_iverilog_dump();
initial begin
    $dumpfile("sim_build/RandomEngine.fst");
    $dumpvars(0, RandomEngine);
end
endmodule
