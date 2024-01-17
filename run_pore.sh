# run  pore calculation in  parallel
nparal=10
frame_per_thread=10
natom=13084
pbs_file=zeo_continous_v2.pbs
traj_file=traj_CAU11_PVDF.gro

for ((i=1; i<=$nparal; i++))
do
  mkdir pore_$i
  cp $pbs_file pore_$i
  cd pore_$i
     ln -s ../$traj_file $traj_file
     sed -i "s/NUMBER/$i/g" $pbs_file
     sed -i "s/NFRAME/$frame_per_thread/g" $pbs_file
     sed -i "s/NATOM/$natom/g" $pbs_file
     sed -i "s/TRAJ_FILE/$traj_file/g" $pbs_file
     start=$(( ($i-1)*(3+$natom)*$frame_per_thread +1 ))
     sed -i  "s/NSTART/$start/g" $pbs_file
     qsub $pbs_file
  cd ../
done

