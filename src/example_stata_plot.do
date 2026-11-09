* Load environment variables
doenv using ".env"

* Define file paths
local output_dir = "`r(OUTPUT_DIR)'"

local output_filepath = "`output_dir'/example_stata_plot.png"

* Display the path to verify
display "`output_filepath'"

* FRED was not selected for this project, so simulate a quarterly GDP series
* to stand in for the one that pull_fred.py would otherwise provide.
clear
set seed 100
set obs 308
gen date_numeric = dofq(tq(1947q1) + _n - 1)
format date_numeric %td
gen gdp = 100 * exp(sum(rnormal(0.008, 0.01)))

* Set the time variable
tsset date_numeric

* Generate the plot
twoway (tsline gdp), title("Simulated GDP over Time") xtitle("Date") ytitle("GDP")
graph export "`output_filepath'", replace

* * Save the plot
* graph export `output_filepath', replace