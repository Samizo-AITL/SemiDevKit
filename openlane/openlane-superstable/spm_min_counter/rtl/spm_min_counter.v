// spm_min_counter.v
module spm_min_counter (
    input  wire       clk,
    input  wire       rst_n,   // active-low synchronous reset
    output reg  [7:0] led
);

    reg [23:0] cnt;

    always @(posedge clk) begin
        if (!rst_n) begin
            cnt <= 24'd0;
            led <= 8'd0;
        end else begin
            cnt <= cnt + 24'd1;
            led <= cnt[23:16];   // slow-ish toggling for observation
        end
    end

endmodule

