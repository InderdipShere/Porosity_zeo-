# Porosity_zeo-
Pore calculation using zeo++ for a region in the system (z-bound) in parallel calculation
It consists of three steps:
1. Preprocessing
   a. get the trajectory file (check the atoms symbol)
   b. ensure python3 and gromacs are working
   c. get the gro2cif.py code to convert .gro file to .cif 
2. Parallel processing
   a. Update zeo_continous_v2.pbs (job name and threshold)
   b. Update run_pore.sh
   c. run script ./run_pore.sh 
3. Post-processing
   a. get compile code to update all the data
   b. use plot_psd.py for plotting the pore size distribution     
