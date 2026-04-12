set term pngcairo size 800,140
set output "killtonda.png" 

unset ytics
set ylabel "INBOUND" rotate by 90

set style data histogram
set style histogram rowstacked
set style fill solid border -1
set boxwidth 0.75 
set xtics rotate by -45

unset key
set yrange [0:*]
plot 'killtonda.dat' using 2:xtic(1) title "YNA" lc rgb "navy" \
    ,'' using 3 title "Newsis" lc rgb "steelblue" \
    ,'' using 4 title "Other" lc rgb "dark-plum"

