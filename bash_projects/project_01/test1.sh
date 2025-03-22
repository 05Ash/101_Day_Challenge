echo "From Home"
ls ~/projects/101_Day_Challenge/bash_projects/project_01/p1
echo "--------------------------"
ls ~/projects/101_Day_Challenge/bash_projects/project_01/p1/d1
echo "--------------------------"
ls ~/projects/101_Day_Challenge/bash_projects/project_01/p1/d1/d12
cd ~/projects/101_Day_Challenge/bash_projects/project_01/p1/d1/d12
echo "From d12"
ls ../..
echo "---------------------------"
ls ../../d2
echo "---------------------------"
ls ../../d2/d22
echo "............................"
cd ..
ls ..
echo "............................"
ls ../d2
echo "............................"
ls ../d2/d21
cd ..
rm -r d1 d2
ls .
