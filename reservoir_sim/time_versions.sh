command=$1
years=50
trials=3
repeat=10

for dir in 'py_cy' 'cy' 'cy_numpy' 'cy_numpy_noCheck'
do
	cd $dir
	$1 setup.py build_ext --inplace
	cd ../
done
echo 
echo 
echo 'Starting timings'
for dir in 'py_slow' 'py_fast' 'py_cy' 'cy' 'numpy' 'cy_numpy' 'cy_numpy_noCheck'
do
	cd $dir
	cp ../time_sim.py .
	$1 time_sim.py $years $trials $repeat $dir
	rm time_sim.py
	cd ../
done
