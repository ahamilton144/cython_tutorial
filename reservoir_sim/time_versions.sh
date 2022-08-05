years=50
trials=4
repeat=20

for dir in 'py_cy' 'cy' 'cy_numpy' 'cy_numpy_reservoir' 'cy_numpy_noCheck'

do
	cd $dir
	python3 setup.py build_ext --inplace
	cd ../
done
echo 
echo 
echo 'Starting timings'
for dir in 'py_slow' 'py_fast' 'py_numpy' 'py_numpy_reservoir' 'py_cy' 'cy' 'cy_numpy' 'cy_numpy_reservoir' 'cy_numpy_noCheck'
do
	cd $dir
	cp ../time_sim.py .
	python3 time_sim.py $years $trials $repeat $dir
	rm time_sim.py
	cd ../
done
